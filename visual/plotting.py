import matplotlib.pyplot as plt
import folium
import streamlit as st

def plot_convergence(history):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(history, linewidth=2, color='#2E86AB')
    ax.set_xlabel('İterasyon', fontsize=12)
    ax.set_ylabel('En İyi Mesafe (km)', fontsize=12)
    ax.set_title('ACO Algoritması Yakınsama Grafiği', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    return fig

def create_route_map(locations, location_names, best_path):
    center_lat = sum(loc[0] for loc in locations) / len(locations)
    center_lon = sum(loc[1] for loc in locations) / len(locations)
    
    m = folium.Map(location=[center_lat, center_lon], zoom_start=14)
    
    for i, (lat, lon) in enumerate(locations):
        folium.Marker(
            [lat, lon],
            popup=f"{i+1}. {location_names[i]}",
            icon=folium.Icon(color='red' if i == 0 else 'blue', icon='info-sign')
        ).add_to(m)
    
    route_coords = [[locations[i][0], locations[i][1]] for i in best_path]
    folium.PolyLine(route_coords, color='green', weight=3, opacity=0.8).add_to(m)
    
    return m

