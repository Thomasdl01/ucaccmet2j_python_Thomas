import json

with open ('precipitation.json') as file:
    Precipitation_Data = json.load(file)
#I opened the Json file and renamed it to the Precipitation variable 
# GHCND:US1WAKG0038 Seattle Station Code

with open('stations.csv') as file:
    Stations_Data = file.read()

# I opened the CSV file and attributed the file to a Stations variable
total_precipitation_monthly = {}
for Rain in Precipitation_Data:
    if Rain["station"] == "GHCND:US1WAKG0038":
        # print(Rain) 
# This for Fucntion prints data points only if they have the Seattle code, they print it from the precipitation_data file.        
        Datum = Rain["date"]
        Datum_Day = Datum.split("-")
        # print(Datum_Day)
            
        month = Datum_Day[1]
        # print(month)
        if month == "01":
            print(month)
                        
            # total_precipitation_monthly = {}
            #for Value in Rain: 
        if month in total_precipitation_monthly:
            total_precipitation_monthly[month] +=Rain["value"]
        else:
            total_precipitation_monthly[month] = Rain["value"]

#                 #In the Functions above I have calculated the precipitation per month in SeattlI have done this by splitting ->
#                 #the date so that we can filter along the value of month. Using teh splitted date we then used the if month functions ->
#                 #and then computed along the months for the values and printed the outcome.
#  Part .2

        jaar = Datum_Day[0]
        print(jaar)

        if jaar in total_precipitation_monthly:
            total_precipitation_monthly [jaar] +=Rain["value"]
        else:
            total_precipitation_monthly[jaar] = Rain["value"]

print(total_precipitation_monthly)

# this was the calculation for the yearly precipitation, done by using the splitted dates from the monthly calculations.

#         total = Datum_Day[2]
#         total >= "01"
#         #calculating for the yearly precipitation, taking what is equal to or more than 01 in months as a total.


# print(total_precipitation_monthly)   
# print(total)             
