person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#1: Check if the person dictionary has skills key, ifso print the middle skill in the skills list.
if 'skills' in person:
    middle_skill = person['skills'][len(person['skills']) // 2]
    print(middle_skill)
else: 
    print("The 'skills' key is not found in the person dictionary.")

#2
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")
else:    print("The 'skills' key is not found in the person dictionary.")

#3
if 'skills' in person:
    if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
        print("She is a fullstack developer.")
    elif 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
        print("She is a backend developer.")
    elif 'JavaScript' in person['skills'] and 'React' in person['skills'] and not any (skill in person['skills'] for skill in ['Node', 'MongoDB', 'Python']):
        print("She is a front end developer.")
    else:
        print("Unknown title.")
else:    print("The 'skills' key is not found in the person dictionary.")

#4
if 'is_married' in person == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")