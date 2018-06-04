import folium
import pandas

# Loading the data from the file Volcanoes.txt
data = pandas.read_csv("Volcanoes.txt")

# Getting the coordinates to a list
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Defining the map and feature group
map = folium.Map([38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

# Adding the markers from the list
for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("Map1.html")
