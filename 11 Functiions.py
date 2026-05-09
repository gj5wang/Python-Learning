# check if a numbe is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        else:
            return True

print(f'the number 11 is prime: {is_prime(11)}')

#3
def check_type(lst):
    if len(lst) <= 1:
        return True
    if type(lst[0]) == type(lst[1]):
        del lst[0]
        return check_type (lst)
    else:
        return False

print(f'all the items in the list have the same data type: {check_type(["a", 2, 3, 4])}')

#5
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
from data import countries_data
def most_spoken_languages(countries, n):
    language_count = {}
    for country in countries:
        for lang in country['languages']:
            if lang in language_count:
                language_count[lang] += 1
            else:
                language_count[lang] = 1
#get the topn, return just the names
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    top_n_languages = [lang[0] for lang in sorted_languages[:n]]
    print(f'Top {n} most spoken languages: {top_n_languages}')