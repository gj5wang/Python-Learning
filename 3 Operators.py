# question 1: Declare your age as integer variable
age = 19

# question 5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print(f'The perimeter of the triangle is: {a + b + c}')

#question 9: Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
y2 = 10
y1 = 2
x2 = 6
x1 = 2
m = (y2 - y1) / (x2 - x1)
print(f'The slope of the line is: {m}')

# question 13: Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# question 20
#int(9.8) returns 9, and 10 is 10, so the statement is false
print(int(9.8) == 10)

# question 23
#e
for i in range(5):
    print(i + 1, 1, i+1, (i + 1) ** 2, (i + 1) ** 3)


