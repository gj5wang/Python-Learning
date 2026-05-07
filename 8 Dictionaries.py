# 1
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'capybara'
dog['color'] = 'brown'
dog['breed'] = 'capybara'
dog['legs'] = 4
dog['age'] = 5
print(dog)

#3
student ={
    'first_name': 'Gloria',
    'last_name': 'blabla', 
    'gender': 'female',
    'age': 19,
    'marital_status': 'single',
    'skills': ['Python', 'JavaScript', 'HTML', 'CSS'],
    'country': 'somewhere', 
    'city': 'somewhere',
    'address': 'somewhere'
}

#4
print(len(student))

#5
print(student['skills'])
print(type(student['skills']))

#6
student['skills'].append('React')
print(student['skills'])

#7
keys = student.keys()
print(keys)

#8
values = student.values()
print(values)

#9 change the dictionary to a list of tuples using items() method
print(student.items())

#10 delete one of the items in the dictionary
del student["city"]
print(student)

#11 delete one of the dictionaries
del dog