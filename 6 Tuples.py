#2
fruits = ('apple', 'banana', 'orange')
vegetables = ('cabbage', 'carrot', 'spinach')
animal_products = ('capybara', 'bunny', 'dog')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3: Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) //2
if (len(food_stuff_lt) % 2 == 0):
  print(f'the list after slicing out the middle item is {food_stuff_lt[: middle_index - 1] + food_stuff_lt[middle_index: + 1]}')
else:
    print(f'the list after slicing out the middle item is {food_stuff_lt[: middle_index] + food_stuff_lt[middle_index + 1:]}')


#5
third_last_index = len(food_stuff_lt) - 3
print(f'the list after slicing out the the first three and last three is {food_stuff_lt [3 : third_last_index]}')

#6 delete the food_stuff_tp tuple completely
del food_stuff_tp