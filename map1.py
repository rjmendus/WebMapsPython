import folium
import pandas

# Loading the data from the file Volcanoes.txt
data = pandas.read_csv("Volcanoes.txt")

# Getting the coordinates to a list
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Returns color for different categories of elevation
def get_elevation_color(elevation):
	if elevation < 1000:
		return "green"
	elif 1000 <= elevation < 3000:
		return "orange"
	else:
		return "red"

# Defining the map and feature group
map = folium.Map([38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

# Adding the markers from the list
for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el) + " m",
		fill_color = get_elevation_color(el), color= "black", fill = True, fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")
