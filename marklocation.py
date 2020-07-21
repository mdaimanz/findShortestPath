from geopy.geocoders import Nominatim
from gmplot import gmplot
from itertools import permutations
import googlemaps

#function that return coordinate with the name of the place as the param
def markLocation(place):
    geolocator = Nominatim(user_agent= "Nominatim")
    location = geolocator.geocode(place)
    place_coordinate = (location.latitude , location.longitude)
    return place_coordinate

def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

#creating google map object
gmaps = gmplot.GoogleMapPlotter(3.1390,101.6869, 6,apikey="AIzaSyCvLnDkcu8HzrrEqpIFdhqYIg2BTTRw1zs")
gmaps.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

place = ["Kuala Lumpur","Bangkok","Jakarta","Seoul","Tokyo","Taipei","Hong Kong","Beijing"]
list_lat=[]
list_lon=[]
Lat = []
Lon =[]
path=[]
all_path=[]

origin = "Kuala Lumpur"

coordinate = markLocation(origin)
(latitude, longitude) = coordinate
lat = latitude
lon = longitude
list_lat.append(latitude)
list_lon.append(longitude)

#loop to mark all places and store their coordinates in an array 'path'
for i in range(len(place)):
    coordinate = markLocation(place[i])
    path.append(coordinate)
    (latitude, longitude) = coordinate
    lat = latitude
    lon = longitude
    Lat.append(latitude)
    Lon.append(longitude)

all_path.append(permutation(path))
#generating all possible path and registered all of them in all_path[]
for p in permutation(path):
    coordinate = p[i]
    (latitude, longitude) = coordinate
    lat = latitude
    lon = longitude
    list_lat.append(latitude)
    list_lon.append(longitude)



gmaps.scatter(Lat,Lon,'#f0dd92',marker="True",size=30)
gmaps.plot(list_lat,list_lon, 'cornflowerblue', edge_width=5)
gmaps.draw("my_map.html")
print("Map generated successfully!")

























