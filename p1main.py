from geopy.geocoders import Nominatim
import googlemaps
from geopy import distance
from flask import Flask
from flask import render_template
from DistanceUtils import getCoordinate,generateMatrix,exportMatrix,generatePossiblePath,calcTotalDist,findMinimum,getMinLng,getMinLat

def main():
    # Requires API key
    gmaps = googlemaps.Client(key='AIzaSyCvLnDkcu8HzrrEqpIFdhqYIg2BTTRw1zs')

    place = ["Kuala Lumpur", "Bangkok", "Jakarta", "Seoul", "Tokyo", "Taipei", "Hong Kong", "Paris","Brunei"]

    nums = [1,2,3,4,5,6,7,8]
    coords = getCoordinate(place)  # generate coordinates for each place
    matrix = generateMatrix(place, coords)  # generate matrix and fills it with distance between each places
    exportMatrix(place,matrix)
    all_path = generatePossiblePath(nums)  # generate all combination of possible paths
    totalDistance = calcTotalDist(matrix, all_path)  # calculate distance for each possible path
    minPath = findMinimum(place,all_path, totalDistance)  # find the path with the least distance travelled

    # loadFlask(minPath,coords) #initiate flask and pass the latitudes & longitudes of the path with the least distance travelled
    #Initiate flask and pass the Lat and Lng value

    Lat = getMinLat(minPath,coords)
    Lng = getMinLng(minPath,coords)
    @app.route("/", methods=['GET','POST'])
    def index():
        data = Lat
        data2 = Lng
        return render_template('polyline.html',data=Lat,data2=Lng)

app = Flask(__name__)

if __name__ == "__main__":
    main()
    app.run(debug=True)
