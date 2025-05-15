# Task 3 Question 1
# Create and print variables
# Create variables of different data types:

print("Task3: Question:1")
name = "srinivas"
age = 23
height = 5.7
is_student = True

# print the variables and their types using type() function
print(name)
print(type(name))
print(age)
print(type(age))
print(height)
print(type(height))
print(is_student)
print(type(is_student))

print()

# Task 3 Question 2
# Assign a number to a variable, then change it to a string. Print the value and type before and after.

# assign a number to a string
print("Task3: Question:2")
a = 10
print("before change:")
print("value: ",a)
print("type: ", type(a))
print()
# change the number to a string
a = str(a)
print("after change:")
print("value: ",a)
print("type:",type(a))
print()

# Task 3 Question 3
# Give a list of values and ask students to guess the datatype before using type() to check:
print("10: int")
print("3.14: float")
print("hello: str")
print("True: bool")
print()

# Task 3 Question 4
# variable name practice
# Ask students to create a variables with meaningful names:

my_name = "srinivas"
marks = 95
myResultStatus = "pass"

print("variable name: my_name")
print("value: ",my_name)
print("variable name: marks")
print("value: ",marks)
print("variable name: myResultStatus")
print("value: ",myResultStatus)
print()

# Task 3 Question 5
# Identify Errors
# Give wrong variable assignments and ask them to correct

print("1name=srinivas: #invalid")
print("my-age=20: invalid")
print("Name: #NameError") 
print()
print("correct variable names:")
print("name1 = srinivas")
print("my_age = 20")
print("Name = 'srinivas'")
print()

# Task 3 Question 6
# Ask students to write a mini-story using variables
print("Task3: Question:6")
hero = "spider-man"
villin = "Green Goblin"
city = "New York"
print(hero, "saved", city, "from", villin)
print()

# Task 3 Question 7
# Create two variables and swap their values

a = 5
b = 10
print("Before swapping:")
print("a =", a)
print("b =", b)
# swap the values
x = a
a = b
b = x
print("After swapping:")
print("a =", a)
print("b =", b)
