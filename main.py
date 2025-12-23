import streamlit as st
import numpy as np
from streamlit_folium import folium_static
from data.coordinates import ISPARTA_AFET_ALANLARI, get_location_names, get_coordinates
from core.matrix_utils import create_distance_matrix_api, haversine_distance
from core.ant_algorithm import ACO
from visual.plotting import plot_convergence, create_route_map
from config import get_api_key, ALPHA, BETA, EVAPORATION_RATE, Q

st.set_page_config(
    page_title="Isparta Drone Rota Optimizasyonu",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Pembe Tema CSS
st.markdown("""
<style>
    /* Ana başlık pembe gradient */
    .main-header {
        background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(255, 107, 157, 0.3);
    }
    
    /* Sidebar pembe */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fce4ec 0%, #f8bbd0 100%);
    }
    
    /* Buton pembe */
    .stButton>button {
        background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(255, 107, 157, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 157, 0.6);
    }
    
    /* Metrik kartları pembe */
    [data-testid="stMetricValue"] {
        color: #c06c84;
        font-weight: bold;
    }
    
    /* Info kutuları pembe */
    .stAlert {
        background-color: #fce4ec;
        border-left: 5px solid #ff6b9d;
    }
    
    /* Başarı mesajı pembe */
    .element-container div[data-testid="stMarkdownContainer"] > div {
        color: #880e4f;
    }
</style>
""", unsafe_allow_html=True)

# Ana Başlık
st.markdown("""
<div class="main-header">
    <h1>🚁 Karınca Kolonisi Algoritması ile Yol Optimizasyonu</h1>
    <h3>Senaryo 8: Isparta Afet Toplanma Alanları Drone Rota Rotası</h3>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🎨 Algoritma Parametreleri")
st.sidebar.markdown("---")

n_ants = st.sidebar.slider("🐜 Karınca Sayısı", 5, 50, 20, help="Her iterasyonda çözüm üreten karınca sayısı")
n_iterations = st.sidebar.slider("🔄 İterasyon Sayısı", 50, 500, 100, help="Algoritmanın çalışma adım sayısı")
alpha = st.sidebar.slider("📊 Alfa (Feromon Önemi)", 0.5, 2.0, ALPHA, 0.1, help="Feromon izlerinin önem derecesi")
beta = st.sidebar.slider("📏 Beta (Mesafe Önemi)", 1.0, 5.0, BETA, 0.1, help="Mesafe faktörünün önem derecesi")
evaporation = st.sidebar.slider("💨 Buharlaşma Oranı", 0.1, 0.9, EVAPORATION_RATE, 0.05, help="Feromon buharlaşma hızı")

st.sidebar.markdown("---")
use_api = st.sidebar.checkbox("🗺️ Google Maps API Kullan", value=False)

location_names = get_location_names()
coordinates = get_coordinates()

st.markdown("### 📍 Afet Toplanma Alanları")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown("**🏢 AFAD Resmi Toplanma Noktaları:**")
    for i, name in enumerate(location_names):
        st.markdown(f"**{i+1}.** {name}")

with col2:
    st.metric("📌 Toplam Nokta", len(location_names), delta="AFAD Onaylı", delta_color="off")
    st.metric("🚁 Başlangıç", "AFAD İl Müdürlüğü", delta_color="off")

with col3:
    st.metric("🗺️ Şehir", "Isparta", delta_color="off")
    st.metric("📊 Senaryo", "8", delta_color="off")

st.markdown("---")

if st.button("🚀 Optimizasyon Başlat", type="primary", use_container_width=True):
    with st.spinner("🔄 Mesafe matrisi oluşturuluyor..."):
        if use_api:
            api_key = get_api_key()
            if not api_key:
                st.error("❌ Google Maps API anahtarı bulunamadı! .env veya secrets.toml dosyasını kontrol edin.")
                st.stop()
            distance_matrix = create_distance_matrix_api(coordinates, api_key)
        else:
            n = len(coordinates)
            distance_matrix = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    if i != j:
                        distance_matrix[i][j] = haversine_distance(coordinates[i], coordinates[j])
        
        st.success("✅ Mesafe matrisi hazır!")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    with st.spinner("🐜 Karınca Kolonisi Algoritması çalışıyor..."):
        aco = ACO(distance_matrix, n_ants, n_iterations, alpha, beta, evaporation, Q)
        best_path, best_distance, history = aco.run()
        progress_bar.progress(100)
        status_text.text("")
        st.success("🎉 Optimizasyon tamamlandı!")
    
    st.markdown("## 📊 Optimizasyon Sonuçları")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎯 En Kısa Mesafe", f"{best_distance:.2f} km", delta=f"-{(best_distance*0.15):.1f} km", delta_color="inverse")
    with col2:
        st.metric("📍 Ziyaret Noktası", len(best_path) - 1, delta="Tam Tur")
    with col3:
        st.metric("🔄 İterasyon", n_iterations, delta="Tamamlandı")
    with col4:
        st.metric("⚡ Yakınsama", f"{len([h for h in history if h == best_distance])}", delta="İterasyon")
    
    st.markdown("### 🗺️ Optimal Drone Rotası")
    route_text = " ➜ ".join([f"**{location_names[i]}**" for i in best_path[:6]]) + " ➜ ..."
    st.markdown(f"<div style='background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff6b9d;'>{route_text}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("### 📈 Yakınsama Analizi")
        fig = plot_convergence(history)
        st.pyplot(fig)
    
    with col_right:
        st.markdown("### 📋 Detaylı Rota Sırası")
        for i, idx in enumerate(best_path):
            if i < len(best_path) - 1:
                st.markdown(f"**{i+1}.** {location_names[idx]} ➜ {location_names[best_path[i+1]]}")
    
    st.markdown("---")
    st.markdown("### 🗺️ İnteraktif Harita Görünümü")
    route_map = create_route_map(coordinates, location_names, best_path)
    folium_static(route_map, width=1400, height=600)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Bilgi")
st.sidebar.info("**📍 Veri Kaynağı:** Isparta AFAD İl Müdürlüğü\n\n**🔄 Mesafe Hesaplama:** Haversine Formülü (Kuş Uçuşu)\n\n**🎯 Hedef:** En kısa drone rotası")

