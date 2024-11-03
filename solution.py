from geopy import distance
import requests
# call api
api_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
response = requests.get(api_url)
terremotos = response.json().get("features")

# filer json
terremotos_dict = {}
for terremoto in terremotos:
	terremotos_dict[terremoto.get("id")] = {
	"titulo": terremoto.get("properties").get("title"),
	"coordenadas": (terremoto.get("geometry").get("coordinates") [1],terremoto.get("geometry").get("coordinates")[0])
}


# calculate the distance of each earthquake to a point (library)

user_lat= 40.730610
user_lon = -73.935242
coords_1 = (user_lat, user_lon)
Earthk_distance={}
for terremoto_id in terremotos_dict:
	coords_2 = terremotos_dict.get(terremoto_id).get("coordenadas")
	distanceE = int(distance.geodesic(coords_1, coords_2).km)
	Earthk_distance [distanceE] = terremoto_id
Earthk_distance_ordenadas = sorted(Earthk_distance.items())[:10]
earthcakes_more_closed = {id: distancia for distancia, id in Earthk_distance_ordenadas}

for terremoto_id in earthcakes_more_closed:
    titulo = terremotos_dict.get(terremoto_id).get("titulo")
    distanceE = earthcakes_more_closed.get(terremoto_id)
    print(f"{titulo} || {distanceE}")

