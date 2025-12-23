<div align="center">

# 🚁 Isparta Afet Toplanma Alanları Drone Rota Optimizasyonu

### Karınca Kolonisi Algoritması ile Acil Durum Lojistik Planlaması

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()
[![GitHub](https://img.shields.io/badge/GitHub-ferhancibik-black.svg)](https://github.com/ferhancibik/ACO_Isparta_Drone)

**Senaryo 8** | Yapay Zeka ve Sezgisel Algoritmalar Dersi Projesi

</div>

---

## 📖 Proje Hakkında

Bu proje, **Isparta AFAD İl Müdürlüğü** tarafından belirlenen 10 resmi afet toplanma alanı arasında acil durum nakliye dronunun en optimal rotasını bulmak için **Karınca Kolonisi Algoritması (ACO)** kullanmaktadır.

Gerçek hayat senaryosunda, afet durumlarında hızlı müdahale için malzeme ve tıbbi ekipman taşıyan drone'ların en kısa sürede maksimum noktaya ulaşması kritik önem taşımaktadır.

### 🎯 Proje Amacı

- ✅ Afet anında tüm toplanma alanlarına en kısa rotada ulaşım
- ✅ Drone batarya ömrünü optimize etme
- ✅ Zaman ve yakıt maliyetini minimize etme
- ✅ Gerçek coğrafi verilerle çalışan algoritma geliştirme

---

## ✨ Özellikler

<table>
<tr>
<td>

### 🧠 Algoritma
- Karınca Kolonisi Optimizasyonu
- Dinamik feromon güncelleme
- Ayarlanabilir hiperparametreler
- Yakınsama analizi

</td>
<td>

### 🎨 Görselleştirme
- İnteraktif Streamlit arayüzü
- Folium harita entegrasyonu
- Real-time yakınsama grafikleri
- Rota animasyonu

</td>
</tr>
<tr>
<td>

### 📍 Veri Kaynağı
- AFAD resmi koordinatları
- 10 stratejik toplanma noktası
- Gerçek enlem/boylam verileri
- Google Maps doğrulama

</td>
<td>

### 🔧 Ek Özellikler
- Google Maps API desteği
- Haversine mesafe hesaplama
- .env güvenlik yapılandırması
- Responsive tasarım

</td>
</tr>
</table>

---

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.8 veya üzeri
- pip paket yöneticisi
- (Opsiyonel) Google Maps API Key

### ⚡ Kurulum

```bash
# Repoyu klonlayın
git clone https://github.com/ferhancibik/ACO_Isparta_Drone.git
cd ACO_Isparta_Drone

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
streamlit run main.py
```

### 🔑 API Yapılandırması (Opsiyonel)

Google Maps API kullanmak için `.env` dosyası oluşturun:

```env
GOOGLE_MAPS_API_KEY=your_api_key_here
```

> **💡 İpucu:** API anahtarı olmadan da çalışır! Haversine formülü ile kuş uçuşu mesafeler hesaplanır.

---

## 📁 Proje Yapısı

```
ACO_Isparta_Drone/
│
├── 📄 main.py                    # Streamlit ana uygulama
├── ⚙️ config.py                  # Yapılandırma ve API ayarları
├── 📋 requirements.txt           # Python bağımlılıkları
├── 📓 proje_notebook.ipynb       # Jupyter notebook demo
├── 📖 README.md                  # Proje dokümantasyonu
│
├── 📂 data/
│   ├── __init__.py
│   └── coordinates.py            # AFAD koordinat veritabanı
│
├── 📂 core/
│   ├── __init__.py
│   ├── ant_algorithm.py          # ACO algoritma implementasyonu
│   └── matrix_utils.py           # Mesafe matrisi hesaplamaları
│
└── 📂 visual/
    ├── __init__.py
    └── plotting.py               # Grafik ve harita görselleştirme
```

---

## 📍 Afet Toplanma Alanları

Isparta AFAD İl Müdürlüğü tarafından belirlenen resmi toplanma noktaları:

| 🏢 No | 📍 Lokasyon | 🌍 Enlem | 🌏 Boylam |
|:---:|-----------|:-------:|:-------:|
| **1** | AFAD İl Müdürlüğü (Başlangıç) | 37.7648 | 30.5566 |
| **2** | Atatürk Stadyumu Toplanma Alanı | 37.7595 | 30.5537 |
| **3** | Kaymakkapı Meydanı | 37.7676 | 30.5519 |
| **4** | 15 Temmuz Demokrasi Meydanı | 37.7632 | 30.5522 |
| **5** | Gülcü Parkı Toplanma Alanı | 37.7588 | 30.5478 |
| **6** | SDÜ Doğu Kampüsü Toplanma Alanı | 37.8456 | 30.5312 |
| **7** | 1500 Evler Parkı | 37.7512 | 30.5598 |
| **8** | Isparta Şehir Hastanesi Alanı | 37.7892 | 30.5234 |
| **9** | Davraz Yolu Toplanma Alanı | 37.7734 | 30.5123 |
| **10** | Ayazmana Mesire Alanı | 37.7498 | 30.5712 |

> 📌 **Kaynak:** Isparta AFAD İl Müdürlüğü

---

## 🎮 Kullanım

### 1️⃣ Parametreleri Ayarlayın

Sol panel üzerinden algoritma parametrelerini özelleştirin:

| Parametre | Açıklama | Önerilen Değer |
|-----------|----------|----------------|
| **Karınca Sayısı** | Her iterasyonda çözüm üreten karınca sayısı | 20 |
| **İterasyon Sayısı** | Algoritmanın çalışma adım sayısı | 100 |
| **Alpha (α)** | Feromon önem katsayısı | 1.0 |
| **Beta (β)** | Mesafe önem katsayısı | 2.0 |
| **Buharlaşma Oranı** | Feromon azalma hızı | 0.5 |

### 2️⃣ Algoritmayı Çalıştırın

"🚀 Rotayı Hesapla" butonuna tıklayarak optimizasyonu başlatın.

### 3️⃣ Sonuçları İnceleyin

- 📊 **En Kısa Mesafe:** Toplam rota uzunluğu (km)
- 🗺️ **Optimal Rota:** Ziyaret sırası
- 📈 **Yakınsama Grafiği:** İterasyon başına iyileşme
- 🗺️ **İnteraktif Harita:** Rota görselleştirmesi

---

## 🧬 Karınca Kolonisi Algoritması (ACO)

### Algoritma Çalışma Prensibi

ACO, doğadaki karıncaların yiyecek ararken bıraktıkları feromon izlerinden ilham alır:

```python
1. Başlangıç: Her karınca rastgele bir rota oluşturur
2. Değerlendirme: Rota mesafeleri hesaplanır
3. Feromon Güncelleme: Kısa rotalar daha fazla feromon alır
4. Buharlaşma: Eski feromonlar zaman içinde azalır
5. Yeni İterasyon: Karıncalar feromon yoğunluğuna göre rota seçer
6. Tekrar: Belirlenen iterasyon sayısı kadar devam eder
```

### Matematiksel Model

**Rota Seçim Olasılığı:**

$$P_{ij} = \frac{[\tau_{ij}]^\alpha \cdot [\eta_{ij}]^\beta}{\sum_{k \in \text{unvisited}} [\tau_{ik}]^\alpha \cdot [\eta_{ik}]^\beta}$$

- `τ` (tau): Feromon yoğunluğu
- `η` (eta): Görünürlük (1/mesafe)
- `α` (alpha): Feromon önem derecesi
- `β` (beta): Mesafe önem derecesi

---

## 🛠️ Teknoloji Stack

<div align="center">

| Kategori | Teknoloji |
|:--------:|:---------:|
| **Programlama Dili** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Web Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| **Veri İşleme** | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) |
| **Görselleştirme** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge) ![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=folium&logoColor=white) |
| **API** | ![Google Maps](https://img.shields.io/badge/Google_Maps-4285F4?style=for-the-badge&logo=google-maps&logoColor=white) |

</div>

---

## 📊 Performans Metrikleri

Algoritma performansı örnek sonuçlar:

| Metrik | Değer |
|--------|-------|
| Toplam Mesafe | ~12.5 km |
| İterasyon Sayısı | 100 |
| Yakınsama Süresi | ~50 iterasyon |
| Çalışma Süresi | <5 saniye |
| Ziyaret Edilen Nokta | 10 + başlangıç |

> ⚠️ **Not:** Değerler algoritma parametrelerine göre değişkenlik gösterebilir.

---

## 🔒 Güvenlik ve Gizlilik

- 🔐 API anahtarları `.env` dosyasında saklanır
- 🚫 `.gitignore` ile hassas veriler repository'ye yüklenmez
- ✅ Her kullanıcı kendi API anahtarını kullanmalıdır
- 📝 Örnek yapılandırma dosyası: `.env.example`

---

## 📚 Ek Kaynaklar

### Akademik Referanslar

- Dorigo, M., & Stützle, T. (2004). *Ant Colony Optimization*. MIT Press.
- Colorni, A., Dorigo, M., & Maniezzo, V. (1992). *Distributed Optimization by Ant Colonies*.

### Faydalı Linkler

- [Streamlit Dokümantasyonu](https://docs.streamlit.io/)
- [Google Maps Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix)
- [Folium Dokümantasyonu](https://python-visualization.github.io/folium/)

---

## 🐛 Sorun Giderme

### Python bulunamadı hatası

```bash
# Python'un kurulu olduğundan emin olun
python --version

# Alternatif olarak
python3 --version
```

### Paket yükleme hatası

```bash
# pip'i güncelleyin
python -m pip install --upgrade pip

# Paketleri tekrar yükleyin
pip install -r requirements.txt
```

### Streamlit açılmıyor

```bash
# Port değiştirerek deneyin
streamlit run main.py --server.port 8502
```

---

## 📈 Geliştirme Yol Haritası

- [ ] Farklı sezgisel algoritma karşılaştırması (GA, PSO)
- [ ] Gerçek zamanlı trafik verileri entegrasyonu
- [ ] Multi-drone koordinasyonu
- [ ] 3D harita görselleştirme
- [ ] Mobil uygulama desteği

---

## 👨‍💻 Geliştirici Bilgileri

<div align="center">

### Ferhan Çıbık

**Okul Numarası:** 2312721038  
**Bölüm:** Bilgisayar Mühendisliği 
**Üniversite:** Isparta Uygulamalı Bilimler Üniversitesi

[![GitHub](https://img.shields.io/badge/GitHub-ferhancibik-black?style=for-the-badge&logo=github)](https://github.com/ferhancibik)
[![Email](https://img.shields.io/badge/Email-ferhancibik9@gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ferhancibik9@gmail.com)

</div>

---

## 📄 Lisans

Bu proje **eğitim amaçlı** geliştirilmiştir ve açık kaynak olarak sunulmaktadır.

---

## 🙏 Teşekkürler

- 📚 Dersi veren hocalarımıza
- 🏛️ Isparta AFAD İl Müdürlüğü'ne veri desteği için
- 🌍 Açık kaynak topluluğuna

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**

Made with ❤️ by [Ferhan Çıbık](https://github.com/ferhancibik)

*Son Güncelleme: Aralık 2025*

</div>
