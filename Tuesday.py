import json

with open ('precipitation.json') as file:
    Precipitation = 'precipitation.json' 
#I opened the Json file and renamed it to the Precipitation variable 
# GHCND:US1WAKG0038 Seattle Station Code

with open('stations.csv') as file:
    Stations = 'stations.csv'

# I opened the CSV file and attributed the file to a Stations variable

for Rain in Precipitation:
    
