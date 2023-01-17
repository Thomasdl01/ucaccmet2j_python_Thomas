import json

with open ('precipitation.json') as file:
    Precipitation = 'precipitation.json' 
    


total_monthly_precipitation = Precipitation["Station"] * Precipitation["Location"]
print(total_monthly_precipitation)