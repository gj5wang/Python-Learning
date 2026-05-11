# map(): 
    # syntax
    # map(function, iterable), apply the function to the parameter(iterable)

# filter():
    # syntax
    # filter(function, iterable) (keep the ones in the interable that passes the function)

#exercise: Use the countries_data.py file and follow the tasks below:
# Sort countries by name, by capital, by population
from data.countries_data import data
countries_sorted_by_name = sorted(data, key=lambda x: x['name'])
print (f'Countries sorted by name: {[country["name"] for country in countries_sorted_by_name]}')

countries_sorted_by_capital = sorted(data, key = lambda x: x['capital'])
print(f'Countried sorted by capital:{[country["capital"] for country in countries_sorted_by_capital]}')

by_population = sorted(data, key = lambda x: x['population'], reverse = True)
print(f'Countries sorted by population: {[country["name"] for country in by_population]}')
# Sort out the ten most spoken languages by location.
from collections import Counter
language_count = Counter()
for country in data:
    for lang in country['languages']:
        language_count[lang] += 1
        most_common_languages = language_count.most_common(10)
print(f'The 10 most spoken languages in the world:{most_common_languages}')

# Sort out the ten most populated countries.
most_populated = sorted(data, key=lambda x: x['population'], reverse=True)[: 10]
print (f'The 10 most populated countries in the world: {[country["name"] for country in most_populated]}')