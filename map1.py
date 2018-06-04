import folium

map = folium.Map([9.9632, 76.2532], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for coordinates in [[9.6, 76.4],[8.6, 75.4]]:
	fg.add_child(folium.Marker(location=coordinates, popup="Hello", icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("Map1.html")
