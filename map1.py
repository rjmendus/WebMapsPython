import folium

map = folium.Map([9.9632, 76.2532], zoom_start=6, tiles="Mapbox Bright")

map.save("Map1.html")
