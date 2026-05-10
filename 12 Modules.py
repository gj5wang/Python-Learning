# 1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5, 6, 7]))

# 2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    import random
    numbers = set()
    while len(numbers) < 7:
        numbers.add(random.randint(0, 9))
    return list(numbers)

print(unique_random_numbers())


from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3