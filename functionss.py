# Loops using Functions

# Write a program to print the sum of all even numbers between 1 and 100

def sum_of_even_numbers(start, end):
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            total += number
    return total
sum_of_even_numbers(1, 100) 

# _______________________________________________________________________________________________________________________________________________-

# # Write a program that prints the first 10 powers of 2 using a loop
def first_10_powers_of_2():
    powers = []
    for i in range(10):
        powers.append(2 ** i)
    return powers
# ______________________________________________________________________________________________________________________________________________________

# # print the reverse of a given numbers
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

# _________________________________________________________________________________________________________________________________________________

# count the number of digits in a given integer using a loop
def func(num):
    count = 0
    while num>0:
        num//=10
        count +=1
    return count
a = func(12345)
print(a)

# _________________________________________________________________________________________________________________________________________________

# write a program that print all numbers from 1 to 100 that are divisible by both 3 and 5

def divisible_by_3_and_5(start, end):
    divisible_numbers = []
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            divisible_numbers.append(number)
    return divisible_numbers

# _________________________________________________________________________________________________________________________________________________

# Without using multiplication, calculate a * b using addition and a loop.

def multiply_using_addition(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result

# _________________________________________________________________________________________________________________________________________________

# Q8. Print the sum of digits of a number entered by the user(e.g: 123 --> 1+2+3 = 6)

def func(num):
    count = 0
    while num>0:
        digit = num%10
        count+=digit
        num = num//10
    return count
a = func(123)
print(a)

# _________________________________________________________________________________________________________________________________________________

# Q9. Write a loop to check if a number is a palindrome 

def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num

# _____________________________________________________________________________________________________________________________________________________

# Q10. Write a program to find the highest digit in a given number

def highest_digit(num):
    highest = 0
    while num > 0:
        digit = num % 10
        if digit > highest:
            highest = digit
        num //= 10
    return highest

# __________________________________________________________________________________________________________________________________________________

                                                                        # CONDITIONALS
                                                                        
# Q11. # Q11. Write a program to check if a number is positive, negative, or zero

def func():
  num = int(input("Enter a number: "))
  if num>0:
    return "Positive"
  elif num<0:
    return "Negative"
  elif num==0:
    return "Zero"
  else:
    return "Give only numbers"
func()

# __________________________________________________________________________________________________________________________________________________

# Q12. Write a program that takes a number and prints whether it is divisible by 2,3, both or neither

def func(num):
  if num%2==0 and num%3==0:
    return "Divisible by both"
  elif num%2==0:
    return "Divisible by 2"
  elif num%3==0:
    return "Divisible by 3"
  else:
    return f"{num} neither divisible by 2 and 3"
func(6)

# __________________________________________________________________________________________________________________________________________________

# Q13. Check if a number is a three-digit number using conditionals
def func(num):
  if num>100 and num<999:
    return(f"{num} is a three digit number")
  else:
    return(f"{num} is not a three digit number")
func(12)
# # __________________________________________________________________________________________________________________________________________________

# Q14. Write a program to check whether a given number is a prime number

def func(num):
  if num<=1:
    return "Prime numbers start from 2"
  for i in range(2,num):
    if num%i==0:
      return f"{num} is not a prime number"
  return f"{num} is a prime number"
func(23)

# ____________________________________________________________________________________________________________________________________________________

# Q15. Write a program to find the largest of three numbers entered by the user using nested if-else

def func():
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  c = int(input("Enter third number: "))

  if a>b:
    if a>c:
      return f"{a} is greater"
    else:
      return f"{c} is greater"
  else:
    if b>c:
      return f"{b} is greater"
    else:
      return f"{c} is greater"
func()
# ______________________________________________________________________________________________________________________________________________________

# Q16. Check if year is leap or not

def leap_year():
  year = int(input("Enter year: "))
  if year%4==0 and year%100!=0 or year%400==0:
    print( f"{year} is leap year")
  else:
    print(f"{year} is not leap year")
leap_year()
# ______________________________________________________________________________________________________________________________________________________

# Q17. Take an integer input and determine if it is even and greater than 50.

def func():
  num = int(input("Enter a number: "))
  if num%2==0 and num>50:
    return f"{num} is even and greater than 50"
  elif num%2==1 and num>50:
    return f"{num} is greater than 50 but not even"
  else:
    return f"{num} is neither even nor greater than 50"
func()
# ______________________________________________________________________________________________________________________________________________________

# Q18
"""
Write a program to classify a number as:

* Less than 0: "Negative"
* 0 to 9: "Single Digit"
* 10 to 99: "Two Digits"
* 100 and above: "Three or More Digits"
"""

def func():
  num = int(input("Enter a number: "))
  if num<0:
    return f"{num} is negative"
  elif num>=0 and num<=9:
    return f"{num} is single digit value"
  elif num>=10 and num<=99:
    return f"{num} is two digit value"
  elif num>=100:
    return f"{num} is three digit value"
func()
# ______________________________________________________________________________________________________________________________________________________

# Q19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square

def func():
  num = int(input("Enter a number: "))
  a = num**2
  if a>1000:
    return a
  else:
    return f"square of {num} is not greater than 1000"
func()

# ______________________________________________________________________________________________________________________________________________________

# Q20. Take two integers as input and determine if one is a factor of the other.

def func():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  if num1 % num2 == 0:
    return f"{num2} is a factor of {num1}"
  elif num2 % num1 == 0:
    return f"{num1} is a factor of {num2}"
  else:
    return f"Neither {num1} nor {num2} is a factor of the other"
# _________________________________________________________________________________________________________________________________________________________


