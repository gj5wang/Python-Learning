# question 1
new = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(new)

# question 5: Print the length of the company string using len() method and print().
company = 'Coding For All'
print(len(company))

# question 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Coding' in company)

# question 15 
print(company[0])

# question 20: Use index to determine the position of the first occurrence of C in Coding For All.
index = company.index('C')

if 'C' in company:
    print(f'index of C is: {index}')

# question 25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
result = []

for word in sentence.split():
    if word != 'because':
        result.append(word)

print(' '.join(result))

# question 30
sentence2 = '   Coding For All      '
print(sentence2[sentence2.find('Coding'):sentence2.find('All') + len('All')])

# question 35
print("radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters squared")

# question 36
print("8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144")