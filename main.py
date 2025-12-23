import streamlit as st
import numpy as np
from streamlit_folium import folium_static
from data.coordinates import ISPARTA_AFET_ALANLARI, get_location_names, get_coordinates
from core.matrix_utils import create_distance_matrix_api, haversine_distance
from core.ant_algorithm import ACO
from visual.plotting import plot_convergence, create_route_map
from config import get_api_key, ALPHA, BETA, EVAPORATION_RATE, Q

st.set_page_config(
    page_title="🚁 Isparta Drone Rota Optimizasyonu",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(255, 20, 147, 0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #FFE4E1 0%, #FFF0F5 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF69B4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 15px 30px;
        font-size: 18px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(255, 20, 147, 0.3);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(255, 20, 147, 0.4);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #FFF0F5 0%, #FFE4E1 100%);
    }
    h1, h2, h3 {
        color: #C71585;
    }
    .info-box {
        background: #FFF0F5;
        border-left: 4px solid #FF69B4;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1 style="margin:0; font-size: 2.5em;">🚁 Isparta Afet Toplanma Alanları</h1>
    <h2 style="margin:10px 0 0 0; font-size: 1.5em;">Drone Rota Optimizasyonu</h2>
    <p style="margin:10px 0 0 0; font-size: 1.1em;">🐜 Karınca Kolonisi Algoritması ile En Kısa Rota Bulma</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%); border-radius: 10px; margin-bottom: 20px;">
    <h2 style="color: white; margin: 0;">⚙️ Algoritma Parametreleri</h2>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 🐜 Karınca Parametreleri")
n_ants = st.sidebar.slider("🐜 Karınca Sayısı", 5, 50, 20, help="Her iterasyonda çözüm üreten karınca sayısı")
n_iterations = st.sidebar.slider("🔄 İterasyon Sayısı", 50, 500, 100, help="Algoritmanın kaç kez çalışacağı")

st.sidebar.markdown("### 🧪 Algoritma Katsayıları")
alpha = st.sidebar.slider("α (Alpha) - Feromon Ağırlığı", 0.5, 2.0, ALPHA, 0.1, help="Feromon izlerinin önem derecesi")
beta = st.sidebar.slider("β (Beta) - Mesafe Ağırlığı", 1.0, 5.0, BETA, 0.1, help="Mesafe bilgisinin önem derecesi")
evaporation = st.sidebar.slider("ρ (Rho) - Buharlaşma Oranı", 0.1, 0.9, EVAPORATION_RATE, 0.05, help="Feromon buharlaşma hızı")

st.sidebar.markdown("### 🗺️ Harita Ayarları")
use_api = st.sidebar.checkbox("📍 Google Maps API Kullan", value=False, help="Gerçek yol mesafeleri için API kullan")

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div class="info-box">
    <h4 style="color: #C71585; margin-top: 0;">💡 Bilgi</h4>
    <p style="font-size: 0.9em; margin: 5px 0;">
    <b>🐜 Karınca Sayısı:</b> Daha fazla karınca = daha iyi arama<br>
    <b>🔄 İterasyon:</b> Daha fazla iterasyon = daha iyi sonuç<br>
    <b>α Alpha:</b> Feromon etkisini artırır<br>
    <b>β Beta:</b> Mesafe etkisini artırır<br>
    <b>ρ Rho:</b> Eski yolları unutma hızı
    </p>
</div>
""", unsafe_allow_html=True)

location_names = get_location_names()
coordinates = get_coordinates()

st.markdown("## 📍 Isparta AFAD Resmi Afet Toplanma Alanları")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown("""
    <div class="metric-card">
        <h4 style="color: #C71585; margin-top: 0;">📋 Toplanma Alanları Listesi</h4>
    """, unsafe_allow_html=True)
    for i, name in enumerate(location_names):
        icon = "🏢" if i == 0 else "📍"
        st.markdown(f"**{icon} {i+1}.** {name}")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3 style="color: #FF1493; margin: 0; font-size: 2.5em; text-align: center;">10</h3>
        <p style="text-align: center; color: #C71585; margin: 5px 0 0 0;"><b>Toplam Nokta</b></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3 style="color: #FF69B4; margin: 0; font-size: 1.2em; text-align: center;">🏢 AFAD</h3>
        <p style="text-align: center; color: #C71585; margin: 5px 0 0 0; font-size: 0.9em;"><b>Başlangıç</b></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_button = st.columns([1, 2, 1])
with col_button[1]:
    calculate_button = st.button("🚀 ROTAYI HESAPLA", type="primary", use_container_width=True)

if calculate_button:
    with st.spinner("⏳ Mesafe matrisi oluşturuluyor..."):
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
    
    with st.spinner("🐜 Karıncalar en iyi rotayı arıyor..."):
        aco = ACO(distance_matrix, n_ants, n_iterations, alpha, beta, evaporation, Q)
        best_path, best_distance, history = aco.run()
        progress_bar.progress(100)
        status_text.empty()
        st.success("🎉 Optimizasyon tamamlandı!")
    
    st.markdown("## 📊 Optimizasyon Sonuçları")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card" style="text-align: center;">
            <h2 style="color: #FF1493; margin: 0; font-size: 2.5em;">{:.2f} km</h2>
            <p style="color: #C71585; margin: 5px 0 0 0;"><b>🎯 En Kısa Mesafe</b></p>
        </div>
        """.format(best_distance), unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card" style="text-align: center;">
            <h2 style="color: #FF69B4; margin: 0; font-size: 2.5em;">{}</h2>
            <p style="color: #C71585; margin: 5px 0 0 0;"><b>📍 Ziyaret Edilen Nokta</b></p>
        </div>
        """.format(len(best_path) - 1), unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card" style="text-align: center;">
            <h2 style="color: #C71585; margin: 0; font-size: 2.5em;">{}</h2>
            <p style="color: #C71585; margin: 5px 0 0 0;"><b>🔄 İterasyon</b></p>
        </div>
        """.format(n_iterations), unsafe_allow_html=True)
    
    st.markdown("## 🗺️ En İyi Drone Rotası")
    route_text = " ➡️ ".join([f"**{location_names[i]}**" for i in best_path])
    st.markdown(f"""
    <div class="info-box">
        <h4 style="color: #C71585; margin-top: 0;">🚁 Optimal Rota Sırası:</h4>
        <p style="font-size: 1.1em;">{route_text}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 📈 Algoritma Yakınsama Analizi")
    fig = plot_convergence(history)
    st.pyplot(fig)
    
    st.markdown("## 🗺️ İnteraktif Harita Görünümü")
    route_map = create_route_map(coordinates, location_names, best_path)
    folium_static(route_map, width=1200, height=600)
    
    st.balloons()

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background: #FFF0F5; padding: 15px; border-radius: 10px; border-left: 4px solid #FF69B4;">
    <h4 style="color: #C71585; margin-top: 0;">ℹ️ Bilgilendirme</h4>
    <p style="font-size: 0.85em; margin: 0;">
    <b>📍 API Olmadan:</b> Kuş uçuşu mesafeler (Haversine)<br>
    <b>🗺️ API İle:</b> Gerçek yol mesafeleri (Google Maps)
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="text-align: center; padding: 10px;">
    <p style="color: #C71585; font-size: 0.9em; margin: 0;">
    <b>Geliştirici:</b> Ferhan Çıbık<br>
    <b>Proje:</b> ACO Drone Rota Optimizasyonu<br>
    <b>GitHub:</b> <a href="https://github.com/ferhancibik/ACO_Isparta_Drone" target="_blank" style="color: #FF1493;">ACO_Isparta_Drone</a>
    </p>
</div>
""", unsafe_allow_html=True)

