from geopy.geocoders import Nominatim
import googlemaps
from geopy import distance
from itertools import permutations
from flask import Flask
from flask import render_template

#Generating coordinate for each place
def markLocation(place):
    geolocator = Nominatim(user_agent= "Nominatim")
    location = geolocator.geocode(place)
    place_coordinate = (location.latitude , location.longitude)
    return place_coordinate

def getCoordinate(place):
    coords =[]
    for i in range(len(place)):
        coords.append(markLocation(place[i]))
    return coords

def generateMatrix(place,coords):
    matrix = []
    # Generating matrix 8x8 with -1, means null
    for i in range(len(place)):
        arr = []
        for j in range(len(place)):
            if (i == j):
                arr.append(0)
            else:
                arr.append(-1)
        matrix.append(arr)

    # Find distance from one place to the other places
    print("Matrix elements:")
    for x in range(len(place)):
        s = x + 1
        for y in range(s, len(place)):
            matrix[x][y] = distance.distance(coords[x], coords[y]).km
            print(x, ",", y, ":", matrix[x][y])
    return matrix


def exportMatrix(place,matrix):
    file = open("distMatrix.txt","w+")
    for x in range (len(place)):
        for y in range(len(place)):
            if(y == (len(place)-1)):
                file.write("%f" %matrix[x][y])
            elif(y == 0):
                file.write("%f," %matrix[x][y])
            else:
                file.write("%f," %matrix[x][y])
        file.write("\r")
    file.close()


def generatePossiblePath(nums):

    all_path = list(permutations(nums,7))
    print("")
    print("Possible path:")
    print(all_path)
    print("")
    print("Total paths: ",len(all_path))
    return all_path

#Calculate total distance for each path and stored them totalDist array
def calcTotalDist(matrix,all_path):
    totalDist = []
    for i in range(len(all_path)):
        curr = list(all_path[i]) #current calculated path
        curr.insert(0,0) #inserting 0 at index 0 since we started from KL
        currDist = 0
        k=1
        for j in range(len(curr)):
           if k == len(curr):
               break
           # print("Current path: ",i,"windows: ",j,k)
           if matrix[curr[j]][curr[k]] == -1:
               currDist+=matrix[curr[k]][curr[j]]
           else:
               currDist+=matrix[curr[j]][curr[k]]

           k+=1
        totalDist.append(currDist)

    print("")
    print(totalDist)
    return totalDist

def findMinimum(place,all_path,totalDist):
    #find the minimum distance
    minDistance = 20000000
    minIndex = 0
    for x in range(len(totalDist)):
        if(totalDist[x]<minDistance):
            minDistance=totalDist[x]
            minIndex = x

    short = list(all_path[minIndex])
    short.insert(0,0)
    shortest=[]
    for x in range(len(short)):
        shortest.append(place[short[x]])


    print("")
    print("The shortest path will be Path",minIndex,"with distance ",minDistance," kilometres in total.")
    print("The shortest path:",shortest)
    print("")
    return short


#Take coordinates of the minimum path and separate latitude and longitude from coordinates
def getMinLat(shortest,coords):
    shortCoord = []
    Lat = []
    for x in range(len(shortest)):
        currCoord = coords[shortest[x]]
        shortCoord.append(currCoord)
        Lat.append(shortCoord[x][0])
    return Lat

def getMinLng(shortest,coords):
    shortCoord = []
    Lng = []
    for x in range(len(shortest)):
        currCoord = coords[shortest[x]]
        shortCoord.append(currCoord)
        Lng.append(shortCoord[x][1])
    return Lng

def main():
    # Requires API key
    gmaps = googlemaps.Client(key='AIzaSyCvLnDkcu8HzrrEqpIFdhqYIg2BTTRw1zs')

    place = ["Kuala Lumpur", "Bangkok", "Jakarta", "Seoul", "Tokyo", "Taipei", "Hong Kong", "Beijing"]

    nums = [1,2,3,4,5,6,7]
    coords = getCoordinate(place)  # generate coordinates for each place
    matrix = generateMatrix(place, coords)  # generate matrix and fills it with distance between each places
    # findminPath(matrix,place)
    # dijkstra(matrix,place)
    exportMatrix(place,matrix)
    all_path = generatePossiblePath(nums)  # generate all combination of possible paths
    totalDistance = calcTotalDist(matrix, all_path)  # calculate distance for each possible path
    minPath = findMinimum(place,all_path, totalDistance)  # find the path with the least distance travelled

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
























