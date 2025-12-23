import streamlit as st
import numpy as np
from streamlit_folium import folium_static
from data.coordinates import ISPARTA_AFET_ALANLARI, get_location_names, get_coordinates
from core.matrix_utils import create_distance_matrix_api, haversine_distance
from core.ant_algorithm import ACO
from visual.plotting import plot_convergence, create_route_map
from config import get_api_key, ALPHA, BETA, EVAPORATION_RATE, Q

st.set_page_config(page_title="Isparta Drone Rota Optimizasyonu", layout="wide")

st.title("🚁 Isparta Afet Toplanma Alanları - Drone Rota Optimizasyonu")
st.markdown("**Karınca Kolonisi Algoritması (ACO) ile En Kısa Rota Bulma**")

st.sidebar.header("⚙️ Algoritma Parametreleri")
n_ants = st.sidebar.slider("Karınca Sayısı", 5, 50, 20)
n_iterations = st.sidebar.slider("İterasyon Sayısı", 50, 500, 100)
alpha = st.sidebar.slider("Alpha (α) - Feromon Ağırlığı", 0.5, 2.0, ALPHA, 0.1)
beta = st.sidebar.slider("Beta (β) - Mesafe Ağırlığı", 1.0, 5.0, BETA, 0.1)
evaporation = st.sidebar.slider("Buharlaşma Oranı", 0.1, 0.9, EVAPORATION_RATE, 0.05)

use_api = st.sidebar.checkbox("Google Maps API Kullan", value=False)

location_names = get_location_names()
coordinates = get_coordinates()

st.subheader("📍 Afet Toplanma Alanları")
col1, col2 = st.columns([2, 1])

with col1:
    for i, name in enumerate(location_names):
        st.text(f"{i+1}. {name}")

with col2:
    st.metric("Toplam Nokta", len(location_names))
    st.metric("Başlangıç Noktası", location_names[0])

if st.button("🚀 Rotayı Hesapla", type="primary"):
    with st.spinner("Mesafe matrisi oluşturuluyor..."):
        if use_api:
            api_key = get_api_key()
            if not api_key:
                st.error("Google Maps API anahtarı bulunamadı! .env veya secrets.toml dosyasını kontrol edin.")
                st.stop()
            distance_matrix = create_distance_matrix_api(coordinates, api_key)
        else:
            n = len(coordinates)
            distance_matrix = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    if i != j:
                        distance_matrix[i][j] = haversine_distance(coordinates[i], coordinates[j])
        
        st.success("Mesafe matrisi hazır!")
    
    with st.spinner("ACO algoritması çalışıyor..."):
        aco = ACO(distance_matrix, n_ants, n_iterations, alpha, beta, evaporation, Q)
        best_path, best_distance, history = aco.run()
        st.success("Optimizasyon tamamlandı!")
    
    st.subheader("📊 Sonuçlar")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("En Kısa Mesafe", f"{best_distance:.2f} km")
    with col2:
        st.metric("Ziyaret Edilen Nokta", len(best_path) - 1)
    with col3:
        st.metric("İterasyon Sayısı", n_iterations)
    
    st.subheader("🗺️ En İyi Rota")
    route_text = " → ".join([location_names[i] for i in best_path])
    st.info(route_text)
    
    st.subheader("📈 Yakınsama Grafiği")
    fig = plot_convergence(history)
    st.pyplot(fig)
    
    st.subheader("🗺️ Harita Üzerinde Rota")
    route_map = create_route_map(coordinates, location_names, best_path)
    folium_static(route_map, width=1200, height=600)

st.sidebar.markdown("---")
st.sidebar.info("**Not:** API kullanmadan kuş uçuşu mesafeler hesaplanır. API ile gerçek yol mesafeleri alınır.")

