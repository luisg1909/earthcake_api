##Software engineer test for european Company. USD 60,000 Year, full remote
Languate python
#earthquakes-nearby
[USGS Earthquake Hazards Program](https://earthquake.usgs.gov/) is an organization that analyzes earthquake hazards around the world. They expose a REST API with the details of recent earthquakes that occurred around the world: location, magnitude, etc.
We would like to write a program that for a given city (we will provide latitude/lon) finds the 10 nearest earthquakes (earthquakes that occurred in the closest proximity of that city).
## Getting the list of earthquakes
The web services to get the earthquakes are located here: https://earthquake.usgs.gov/earthquakes/feed/v1.0/ geojson.php
We are interested in all earthquakes that occurred in the last 30 days: https://earthquake.usgs.gov/earthquakes/feed/v1. 0/summary/all_month.geojson
For each earthquake there is a lat/lon location of that earthquake. We would like the program to connect to this web service and get the earthquake data.
## Calculating distance
We expect the program to correctly calculate the curve distance between two lat/lon points.
## Program input
The program should accept two numbers on standard input: the latitude and longitude of a city. So for New York the program should start with the numbers
40.730610
-73.935242
Source: https://www.latlong.net/place/new-york-city-ny-usa-1848.html
## Program output
As output, we want the program to list **10** earthquakes that occurred in the closest proximity to the input point, in the order from closest to farthest. For each earthquake we want to print the contents of a "title" field followed by "||" and "distance" (rounded to whole kilometers).
title || distance
title || distance
title || distance
