# 1
sum = 0
for i in range(0, 101):
    sum += i
print(f'The sum of all numbers from 0 to 100 is: {sum}')

# 2
sum_of_evens = 0
sum_of_odds = 0
for i in range (0, 101, 2):
    sum_of_evens += i
for i in range (1, 101, 2):
    sum_of_odds += i
print(f'The sum of all even numbers from 0 to 100 is: {sum_of_evens}'
      f'\nThe sum of all odd numbers from 0 to 100 is: {sum_of_odds}')

# level 3
#question 1
from data.countries import countries
country_with_land = []
for country in countries:
    if ('land' in country):
        country_with_land.append(country)
print(f'Countries with "land" in their name: {country_with_land}')

#q 3 part a
from data.countries_data import data
language = set() #don't use {} because it creates ditionary
for country in data:
    for lang in country['languages']:
        language.add(lang)
print(f'the total number of Unique languages in the world: {len(language)}')

#part b: find the 10 most spoken languages
from collections import Counter
language_count = Counter()
for country in data:
    for lang in country['languages']:
        language_count[lang] += 1
most_common_languages = language_count.most_common(10)
print("The 10 most spoken languages in the world:")
for lang, count in most_common_languages:
    print(f"{lang}: {count} countries")

#part c: find the 10 most populated countries
population_count = Counter()
for country in data:
    population_count[country['name']] += country['population']
most_common_countries = population_count.most_common(10)
print("The 10 most populated countries in the world:")
for country, pop in most_common_countries:
    print(f"{country}: {pop}")