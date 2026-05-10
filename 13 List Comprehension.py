# list comprehension syntax
# [expression for i in iterable if condition]
# Example: Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# lambda function
# syntax
# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))
# example
add = lambda a, b: a + b #basically lambda, parameter, operation
print(add(5, 3))  # Output: 8

#Exercise: 1, 3, 5, 7
# 1: Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter = [i for i in numbers if i <= 0]
print(filter)

#3: Filter only negative and zero in the list using list comprehension
# [(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807)
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

table = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(table)

#5 Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country[0][0], 'city': country[0][1]} for country in countries]
print(countries_dict)
#7 write a lambda function which can solve a slope or y-intercept of linear functions
slope = lambda x1, y1, x2, y2: (x1 - x2) / (y1 - y2)
print(slope(2, 2, 6, 10))