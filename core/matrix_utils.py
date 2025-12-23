import googlemaps
import numpy as np
import time

def create_distance_matrix_api(locations, api_key):
    gmaps = googlemaps.Client(key=api_key)
    n = len(locations)
    distance_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                try:
                    result = gmaps.distance_matrix(
                        origins=[locations[i]],
                        destinations=[locations[j]],
                        mode='driving'
                    )
                    
                    if result['rows'][0]['elements'][0]['status'] == 'OK':
                        distance_matrix[i][j] = result['rows'][0]['elements'][0]['distance']['value'] / 1000
                    else:
                        distance_matrix[i][j] = haversine_distance(locations[i], locations[j])
                    
                    time.sleep(0.1)
                except:
                    distance_matrix[i][j] = haversine_distance(locations[i], locations[j])
            else:
                distance_matrix[i][j] = 0
    
    return distance_matrix

def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371
    
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat/2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    return R * c

