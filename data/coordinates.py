ISPARTA_AFET_ALANLARI = {
    "Doğancı Parkı": (37.7648, 30.5566),
    "Mimar Sinan Parkı": (37.7642, 30.5501),
    "Hastane Yanı Yeşil Alan": (37.7678, 30.5489),
    "Atatürk Stadyumu": (37.7589, 30.5432),
    "Gül Bahçesi Parkı": (37.7703, 30.5545),
    "Kaymakkapı Parkı": (37.7715, 30.5612),
    "Meydan Parkı": (37.7625, 30.5523),
    "Serdar Mahallesi Parkı": (37.7582, 30.5398),
    "Vali Konağı Meydanı": (37.7655, 30.5535),
    "Hızırbey Camii Alanı": (37.7691, 30.5578),
    "Yayla Mahallesi Parkı": (37.7634, 30.5601),
    "Süleyman Demirel Parkı": (37.7721, 30.5523)
}

def get_location_names():
    return list(ISPARTA_AFET_ALANLARI.keys())

def get_coordinates():
    return list(ISPARTA_AFET_ALANLARI.values())

