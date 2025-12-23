# 🚁 Isparta Afet Toplanma Alanları - Drone Rota Optimizasyonu

Karınca Kolonisi Algoritması (ACO) kullanarak Isparta'daki afet toplanma alanları arasında en kısa drone rotasını bulan uygulama.

## 📋 Özellikler

- ✅ 10 resmi AFAD afet toplanma alanı için rota optimizasyonu
- ✅ Karınca Kolonisi Algoritması (ACO) implementasyonu
- ✅ Google Maps API entegrasyonu (opsiyonel)
- ✅ Interaktif Streamlit arayüzü
- ✅ Harita üzerinde görselleştirme
- ✅ Algoritma parametrelerini dinamik ayarlama
- ✅ Yakınsama grafiği

## 🚀 Kurulum

### 1. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

### 2. Google Maps API Anahtarı (Opsiyonel)

Google Maps API kullanmak istiyorsanız:

1. [Google Cloud Console](https://console.cloud.google.com/) adresine gidin
2. Yeni proje oluşturun
3. **Distance Matrix API** ve **Maps JavaScript API**'yi etkinleştirin
4. API anahtarı oluşturun
5. `.env` dosyası oluşturun:

```env
GOOGLE_MAPS_API_KEY=your_api_key_here
```

**Alternatif:** `.streamlit/secrets.toml` dosyası oluşturun:

```toml
GOOGLE_MAPS_API_KEY = "your_api_key_here"
```

**Not:** API anahtarı olmadan da çalışır (kuş uçuşu mesafe ile).

## 💻 Çalıştırma

```bash
streamlit run main.py
```

## 📁 Proje Yapısı

```
aco_ilac_rutasi/
├── main.py                 # Ana Streamlit uygulaması
├── config.py              # Yapılandırma ayarları
├── requirements.txt       # Python bağımlılıkları
├── data/
│   └── coordinates.py     # Isparta afet alanları koordinatları
├── core/
│   ├── ant_algorithm.py   # ACO algoritması
│   └── matrix_utils.py    # Mesafe matrisi hesaplama
├── visual/
│   └── plotting.py        # Görselleştirme fonksiyonları
└── README.md
```

## 🎯 Kullanım

1. Uygulamayı çalıştırın
2. Sol panelden algoritma parametrelerini ayarlayın:
   - Karınca sayısı
   - İterasyon sayısı
   - Alpha (α) - Feromon ağırlığı
   - Beta (β) - Mesafe ağırlığı
   - Buharlaşma oranı
3. "Rotayı Hesapla" butonuna tıklayın
4. Sonuçları inceleyin:
   - En kısa mesafe
   - Optimal rota sırası
   - Yakınsama grafiği
   - Harita üzerinde görselleştirme

## 📍 Afet Toplanma Alanları

Isparta AFAD tarafından belirlenen resmi afet toplanma alanları:

| No | Lokasyon | Enlem | Boylam |
|----|----------|-------|--------|
| 1 | AFAD İl Müdürlüğü (Başlangıç) | 37.7648 | 30.5566 |
| 2 | Atatürk Stadyumu Toplanma Alanı | 37.7595 | 30.5537 |
| 3 | Kaymakkapı Meydanı | 37.7676 | 30.5519 |
| 4 | 15 Temmuz Demokrasi Meydanı | 37.7632 | 30.5522 |
| 5 | Gülcü Parkı Toplanma Alanı | 37.7588 | 30.5478 |
| 6 | SDÜ Doğu Kampüsü Toplanma Alanı | 37.8456 | 30.5312 |
| 7 | 1500 Evler Parkı | 37.7512 | 30.5598 |
| 8 | Isparta Şehir Hastanesi Alanı | 37.7892 | 30.5234 |
| 9 | Davraz Yolu Toplanma Alanı | 37.7734 | 30.5123 |
| 10 | Ayazmana Mesire Alanı | 37.7498 | 30.5712 |

**Not:** Koordinatlar Isparta AFAD İl Müdürlüğü'nden alınmıştır.

## 🔬 Algoritma Detayları

**Karınca Kolonisi Optimizasyonu (ACO):**
- Doğadaki karınca davranışlarından esinlenilmiştir
- Feromon izleri ile en iyi rotayı bulur
- Parametreler:
  - `α (alpha)`: Feromon önem derecesi
  - `β (beta)`: Mesafe önem derecesi
  - `ρ (rho)`: Feromon buharlaşma oranı
  - `Q`: Feromon miktarı sabiti

## 🔒 Güvenlik

- `.env` ve `.streamlit/secrets.toml` dosyaları `.gitignore` ile korunur
- API anahtarlarınızı asla GitHub'a yüklemeyin
- Her geliştirici kendi API anahtarını kullanmalıdır

## 📊 Değerlendirme Kriterleri

- ✅ Veri Hazırlığı ve API Kullanımı (20 puan)
- ✅ ACO Algoritması (30 puan)
- ✅ Streamlit Arayüzü (25 puan)
- ✅ GitHub Teslimi ve Dökümantasyon (15 puan)
- ✅ Sözlü Sunum (10 puan)

## 👨‍💻 Geliştirici

**Ad Soyad:** [Adınızı buraya yazın]  
**Okul No:** [Numaranızı buraya yazın]  
**GitHub:** [Repo linkinizi buraya yazın]

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

