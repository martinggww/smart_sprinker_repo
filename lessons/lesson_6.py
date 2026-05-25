# define a list called 'cities'
# this list contains beijing, shanghai, mclean, dc
# cities = ["Beijing", "Shanghai", "Mclean", "0Beijing"]
# for city in cities:
#     print(city)
# # define a variable called "DC"
# # assign the variable with the 4th element of cities
# DC = cities[3]
# Mclean = cities[2]
#
# #define a list called numbers
# # numbers contains 4,5,8,0,-1
# numbers = [4,5,8,0,-1]
# numbers.sort()
# print(numbers)
# sorted_cities = sorted(cities)
# print(sorted_cities)
#
# cities.append("Houson")
# print(cities)

# data types
# int, string, list, float
weather1 = {
    "city": "Shanghai",
    "temp": 28,
    "is_raining": False
}
weather2 = {
    "city": "Mclean",
    "temp": 30,
    "is_raining": True
}
weather3 = {
    "city": "DC",
    "temp": 31,
    "is_raining": False
}
weathers = [weather1, weather2, weather3]

# Iterate/loop this weathers, ONLY print the city name if the temperature is >= 30 and is_raining == True
for weather in weathers:
    temp = weather["temp"]
    raining = weather["is_raining"]
    if temp >= 30 and raining == True:
        city = weather["city"]
        print(city)

