ISPARTA_AFET_ALANLARI = {
    "AFAD İl Müdürlüğü (Başlangıç)": (37.7648, 30.5566),
    "Atatürk Stadyumu Toplanma Alanı": (37.7595, 30.5537),
    "Kaymakkapı Meydanı": (37.7676, 30.5519),
    "15 Temmuz Demokrasi Meydanı": (37.7632, 30.5522),
    "Gülcü Parkı Toplanma Alanı": (37.7588, 30.5478),
    "SDÜ Doğu Kampüsü Toplanma Alanı": (37.8456, 30.5312),
    "1500 Evler Parkı": (37.7512, 30.5598),
    "Isparta Şehir Hastanesi Alanı": (37.7892, 30.5234),
    "Davraz Yolu Toplanma Alanı": (37.7734, 30.5123),
    "Ayazmana Mesire Alanı": (37.7498, 30.5712)
}

def get_location_names():
    return list(ISPARTA_AFET_ALANLARI.keys())

def get_coordinates():
    return list(ISPARTA_AFET_ALANLARI.values())

