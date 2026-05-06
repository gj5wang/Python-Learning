# q1: Declare an empty list
lst =[]

#q5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['G', 19, 'im not telling you', 'single', 'somewhere']

#q26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
print(joined)

#q27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = joined.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

#Level 2 q1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort
print("Sorted:", ages)
min_age = min (ages)
max_age = max (ages)
print("Min age:", min_age)
print("Max age:", max_age)

#add min_age and max_age to ages list and sort it again
ages.append(min_age)
ages.append(max_age)
ages.sort()
print("Sorted after adding min and max:", ages)

#find median
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Median age:", median)

#find average age
sum = 0
for age in ages:
    sum += age
average = sum / len(ages)
print("Average age:", average)

#range
print(f'The range of ages is: {max_age - min_age}')

absolute_diff = abs(min_age - average)
print(f'The absolute difference between min age and average age is: {absolute_diff}')

