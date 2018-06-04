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
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population Density")

# Adding the markers from the list
for lt, ln, el in zip(lat, lon, elev):
	fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el) + " m",
		fill_color = get_elevation_color(el), color= "black", fill = True, fill_opacity=0.7))

# Opening the GeoJson file
geo_json = open("world.json", "r", encoding="utf-8-sig")

# Adding the polygons to map
fgp.add_child(folium.GeoJson(data=geo_json.read(),
	style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
	else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)

# Adding layer control
map.add_child(folium.LayerControl())

map.save("Map1.html")
