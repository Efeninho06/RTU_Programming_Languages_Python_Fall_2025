"""
Lab 3.1 | Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.
"""

# TODO: Create the datasets
temperatures = [6, 8, 7, 10, 9, 11, 5]  # one week daily temperatures

city_population = {
    "Riga": 632670,
    "Daugavpils": 80467,
    "Liepaja": 68688,
    "Jelgava": 55472,
    "Jurmala": 49463,
}

# TODO: Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)

largest_city = ""
largest_population = 0
for city, pop in city_population.items():
    if pop > largest_population:
        largest_city = city
        largest_population = pop

total_population = sum(city_population.values())

# TODO: Print results
print("Average temperature:", average_temperature)
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
