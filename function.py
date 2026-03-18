#what is function?
#A function is a block of code that runs only when it is called

# syntax
#def function_name():
    # code

#why we use function 
#1, Avoid reapeting code

# #example
# def greet():
#     print("Hello students")

# greet()

# #function with paramaters
# #used for pass values

# def greet(name="student"):
#     print("hello", (name))
# greet()
# greet("shreyarth")

# def add(a,b):
#     return a + b
# result = add(2,3)
# print(result)

# #Task 1
# #create a function to calculate and return 
# def calculate(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "sub":
#         return a - b
#     elif operation == "mul":
#         return a * b
#     elif operation == "div":
#         return a / b
#     else:
#         return "invalid operation"

# print(calculate(10, 5, "add"))
# print(calculate(10, 5, "mul"))

# #Task 2
# #create a function to check if a number is even or odd


# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(check_even_odd(10))
# print(check_even_odd(7))


# # task 3 
# # factorial 

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact

# print(factorial(5))


# # task 4
# # Create a function to find the maximum of number

# def find_max(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(find_max(10, 25, 15))

# # task 5
# #creat a fuction palindrome 

# def palindrome(s):
#     if s == s[::-1]:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"

# # function call
# print(palindrome("madam"))
# print(palindrome("hello"))


# # task 6 
# # create a fuction area of circle 
# def area_circle(r):
#     area = 3.14 * r * r
#     return area

# # function call
# print(area_circle(5))