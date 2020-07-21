# findShortestPath
 Finding a shortest path that includes all destination given with an initial starting point.
 
 Problem Description:
 
 A broker who is looking for industrial investment opportunities in the cities of Asia. He already invested in a company in Kuala Lumpur and now he plans to travel to several cities in Asia from Kuala Lumpur to expand his investment. The cities include Jakarta, Bangkok, Taipei, Hong Kong, Tokyo, Beijing and Seoul. We are assuming that he/she travel by plane and the plane moves in a straight line.
 
 Solution:
 
 1) Mark all designated location and create a polyline consisting of all possible paths. A HTML file 'my_map.html' will be generated. geopy and gmplot packages are required to run marklocation.py.

.. image::  https://drive.google.com/uc?id=17YJGhRgV5tE9tWozm7sxFW8YOSju3lSb&export=download

 2) Generate matrix to store distances between places. The distances are obtained using geopy distance.distance method. Distances return in kilometres unit. As for this      process, each place was referred as code number as shown below:-
     
    Kuala Lumpur - 0
    Bangkok - 1
    Jakarta - 2
    Seoul - 3
    Tokyo - 4
    Taipei - 5 
    Hong Kong - 6
    Beijing - 7
 
 Visual representation of the matrix is shown below:-
 
 .. image::  https://drive.google.com/uc?id=1LV6hkgg94_gO-xeveMToyQeKYBKIG0kJ&export=download
 
 Note: Dist(0)(1) means distance between Kuala Lumpur and Bangkok
 
 3) Generate all possible path. For this method, permutation is used.
 
 4) Calculate total distance for each of all paths.
 
 5) Compare all total distances acquired and find the path with the least distance.
 
  .. image::  https://drive.google.com/uc?id=15_xOBtGipkLrfEwCtP27sjtMHz64Disr&export=download
 
 6) Initiate flask and polyline for the shortest path will be shown on the map.
 
 .. image::  https://drive.google.com/uc?id=1rIWwdOlpdcNzTI3E7qQ_u39eO-9l_cx0&export=download
 
 

