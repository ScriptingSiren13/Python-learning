# 1. A simple Python function 
# def fun():
#  print("Welcome to GFG")

#2. Calling a  Python Function
# #After creating a function in Python we can call it by using the name of the function followed by parenthesis containing parameters of that particular function.
# fun()


#3. Python Function with Parameters:
# def add(num1,num2):
#     num3=num1+num2
#     return num3

# ans=add(1,3)
# print({ans})
# def  myfunc(fname):
#     print(fname+"bhat")

# myfunc("Zarnain")
# myfunc("Rabiya")
# myfunc("Zeenat")

#4. Types of Python Function Arguments
# Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following 4 types of function arguments.
# Arguments:

#a. Default argument
#b. Keyword arguments (named arguments)
#c. Positional arguments
#d. Arbitrary arguments (variable-length arguments *args and **kwargs)

#1. Default Arguments:
# A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. 
# ex1. The following example illustrates Default arguments. 

# def xyz(x,y=60):
#  print("x: ", x, "and y is :", y)

# xyz(10)                #x:  10    y:  60

#2. ex:
# def fam(x,y="zeenat"):
#     print("dad's name is " + x + " and mom's name is "+y)
# fam("zulfi")    #o/p: dad's name is zulfi and mom's name is zeenat


# 2. Keyword Arguments:
#  The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
#ex 1:
# def student(firstname,lastname):
#     print(firstname,lastname)

# student(firstname="Zedd", lastname="Bee")  #Zedd Bee
# student(lastname="Bee",firstname="Eff")    #Eff Bee

#ex 2:
# def sisters(name, age):
#     print(age, name)
# sisters(name="Rabiya", age=19)
# sisters(age=16, name="Ayerah")

# -To specify that a function can have only keyword arguments, add *, before the arguments:
# def myfunc(*,x):
#       print(x)
      
# myfunc(x=4)            #output: 4
# myfunc(4)                #error

# 2. EX:
# def mother(*,mom):
#     print(mom)
# mother(mom="zeenat")  #zeenat
# mother("zeenat")     #error


#3. Positional Arguments:
# We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age. By changing the position, or if you forget the order of the positions, the values can be used in the wrong places,
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:

# def greet(name,/,greeting='Hello',punctuation='!'):
#       print(f"{greeting},{name},{punctuation}")
      

# greet('john')
# greet('Alice','Hi')
# greet(name='Zedd')      #error
# # # greet('Zedd',punctuation='!!!')
# # greet(name='Zedd',punctuation='!!!')    #error:This usage is invalid because name is marked as a positional-only parameter using /, and trying to provide it as a keyword argument will result in a SyntaxError.

#EX 2:
# def car(x,/):
#       print(x)

# car(x=3)  #error
# car(3)

# EX 3:
# def xyz(name,age):
#     print("Hi my name is ", name, " and my age is ", age)

# print("Case 1")
# xyz("Zedd", 22)

# print("CASE 2:")
# xyz(22, Zedd)       

#O/P: Case 1
# Hi my name is  Zedd  and my age is  22
# CASE 2:
# Traceback (most recent call last):
#   File "c:\Users\HP\OneDrive\Desktop\Python\functions.py", line 55, in <module>        
#     xyz(22, Zedd)
#             ^^^^
# NameError: name 'Zedd' is not defined

#Combine Positional-Only and Keyword-Only: You can combine the two argument types in the same function.
#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
#EX 1:
#def myfunc(a,b,/,*,c,d):
#       print(a+b+c+d)

# myfunc(4,5,c=6,d=8)

#EX 2:

# def fam(grandma, grandpa, /,*, mom, dad):
#     print("grandma's name is "+ grandma + " , grandpa's name is "+ grandpa + " , mom's name is "+ mom + " , and dad's name is " + dad)
# fam("naseema", "maqbool", mom="zeenat", dad="zulfikar")   #O/P: grandma's name is naseema , grandpa's name is maqbool , mom's name is zeenat , and dad's name is zulfikar


#4. Arbitrary Keyword  Arguments:
# In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

#1. *args in Python (Non-Keyword Arguments)
# 2. **kwargs in Python (Keyword Arguments)

#Arbitrary Arguments, *args :If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# def mykids(*kids):
#       print("The youngest child is " +kids[1])
# mykids("Zeffu","Faizu")



#Example 1: Variable length non-keywords argument 
# def myFunc(*big):
#     for x in big:
#         print(x)

# myFunc('hello','Welcome', 'to',"Zedd's world")
# OUTPUT: it prints each string argument on a new line

#Example 2: Variable length keyword arguments:
# def myFunc(**kwargs):
#     for x,y in kwargs.items():
#         print("%s==%s" %(x,y))

# myFunc(first='Geeks', mid='for',last='Geeks')


# #Example: Adding Docstring to the function:
# def OddEven(x):
#    """Function to check if the number is even or odd."""
#    if (x%2==0):
#         print("even")
#    else:
#         print("Odd")
# print(OddEven.__doc__)
# OddEven(5)

# Ex2:
# def PosNeg(x):
#     """To check if a number is  positive or  negative"""
#     if x<0:
#         print("X is a negative number")
#     elif x>0:
#         print("x is  posituve number")
#     else:
#         print("x is a while number")
# print(PosNeg.__doc__)
# PosNeg(-3)

#5. Python Function within Functions:
#A function that is defined inside another function is known as the inner function or nested function. Nested functions can access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function.
# def f1():
#     s="I love Python"
#     def f2():
#         print(s)
#     f2()
# f1()
# EX 2:

# def parents():
#     s="Zeenat"
#     i="Zulfikar"
#     def children():
#         print("Father of zedd is "+ i+ " and mother of zedd is "+s)
#     children()
# parents()

#6. Anonymous Functions in Python:
#In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

# def cube(x):
#     return x*x*x
# cube1=lambda x: x*x*x

# print(cube(7))           #343
# print(cube1(7))          #343 

#7. Recursive Functions in Python:
#Recursion in Python refers to when a function calls itself. There are many instances when you have to build a recursive function to solve Mathematical and Recursive Problems.
#Using a recursive function should be done with caution, as a recursive function can become like a non-terminating loop. It is better to check your exit statement while creating a recursive function.
    
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(3))              #Output:6

# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("\n\nRecursion example result")
# tri_recursion(6)




#8. Return Statement in Python Function:
# The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller. The syntax for the return statement is:

# return [expression_list]
# The return statement can consist of a variable, an expression, or a constant which is returned at the end of the function execution. If none of the above is present with the return statement a None object is returned.

#a. Example: Python Function Return Statement:
# def squareValue(num):
#     return num*num
# print(squareValue(4))  #16
# print(squareValue(-3))  #9

#9. Pass by Reference and Pass by Value:
#One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.
# def myFun(x):
#     x[0]=20
# lst=[10,12,14,16,18]
# myFun(lst)
# print(lst)              #O/P:[20, 12, 14, 16, 18]

#When we pass a reference and change the received reference to something else, the connection between the passed and received parameters is broken. For example, consider the below program as follows:
# def myfunc(x):
#     x=[20,30,40]

# lst=[10,11,12,13,14]
# print(myfunc(lst))     #None
# print(lst)             #[10, 11, 12, 13, 14]

#Another example demonstrates that the reference link is broken if we assign a new value (inside the function).
# def myFun(x):
#     x=20
    
# x=10
# myFun(x)
# print(x)

# def swap(x, y):
# 	temp = x
# 	x = y
# 	y = temp


# # Driver code
# x = 2
# y = 3
# swap(x, y)
# print(x)
# print(y)

