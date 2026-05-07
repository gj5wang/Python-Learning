# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

ages_set = set(age)
print(ages_set)

#the list is longer because it has duplications
if (len(ages_set) > len(age)):
    print("The set is larger than the list.")
else:
    print("The list is larger than the set.")

# the difference between the data types: string, list, tuple, and set
# string: an ordered collection of characters that is immutable
# list: an ordered collection of items that is mutable
# tuple: an ordered collection of items that is immutable
# set: an unordered collection of unique items that is mutable

# question 3
sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
unique_words = set(words)
print(f"There are {len(unique_words)} unique words in the sentence.")