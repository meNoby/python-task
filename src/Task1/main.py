import random
from weatherclass import Weather

weather_list = []

# CREATE A LIST OF WEATHER ENTRIES
for i in range(20):
    rand_weather = Weather(f"{i+1}.02.23",
                           random.randint(-10, 10),
                           random.randint(752, 767),
                           "major" if random.random() > 0.8 else "minor" if random.random() > 0.5 else "none")
    weather_list.append(rand_weather)

# LOWEST PRESSURE FOUND
def max_pressure_delta(arr):
    lo = Weather(0, 0, 1000, 0)
    hi = Weather(0, 0, 0, 0)
    for i in arr:
        lo = i if lo.pressure > i.pressure else lo
        hi = i if hi.pressure < i.pressure else hi
    return hi, lo

highest, lowest = max_pressure_delta(weather_list)

# ITERATE THROUGH A LIST
for i in weather_list:
    print(i, "\n")

print(f">>> Highest pressure delta days <<< \n Highest \n{highest}\n Lowest \n{lowest}")