#1. An "if statement" is written by using the if keyword:
#Ex 1:
# a=67
# b=45
# if a > b:
#     print("A is greater than B")

#Ex 2:
# v=10
# if v>15:
#     print("V is greater than 15")
# print("I am not in if block ")  #I am not in if block 



#2. ELSE:
#The else keyword catches anything which isn't caught by the preceding conditions.
#Ex 1:
# b=18
# if b<10:
#     print("Firstly, I am in the 'if' block.")
#     print("B is not less than 10")
# else:
#     print("Firstly, I am in 'else' block")  #Firstly, I am in 'else' block
#     print("b is not less than 10") #b is not less than 10
# print(" I am neither in 'if' block nor in 'else' block.")  #I am neither in 'if' block nor in 'else' block.



#Ex 2:
# a=99
# b=23
# if a>b:
#     print("A is greater than b")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("A is lesser than b")
  
  #You can also have an else without the elif:

#3. Nested if statement:
#Example1 :
# i=25
# if i<21:
#     if i<18:
#         print("I can't drive or I can't drink")
#     else:
#         print("I can drink and I can drive as well, but hey! not simultaneously :)")
# else:
#     print(" I can do whatever I want, of course it must be legal, Duhhh")

# Output:
# I can do whatever I want, of course it must be legal, Duhhh

#You can have if statements inside if statements, this is called nested if statements.

# age=int(input("Enter your age"))

# if age>=18:
#  print("You are eligible to vote")
#  if age>=21:
#     print("You can have alcohol")
#  else:
#     print("you cannot purchase alcohol but you can still vote") 

#Example 2:
# else:
#   print("you cannot vote")  


#4. Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

#Example 1:
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

#Example 2: 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")    #a and b are equal
else:
  print("a is greater than b")


#4. Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
# a=95
# b=65
# if a <b : print("a is less than b")
# if a > b:print("a is greater than b")

#5.Short Hand If ... Else
#Example 1: If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# a=27
# b=55
# print("a is greater than b") if a>b else print("b is greater than a") 
# print("a is less than b") if a<b else print("a is greater than b")   # Output: a is less than b
# This technique is known as Ternary Operators, or Conditional Expressions.

#Example 2: One line if else statement, with 3 conditions:
# print("A is greater than B") if a>b else print("A is equal to B") if a==b else print("B is greater than A")   #output: B is greater than A
# print(" a is less than b")if a<b else print("a is equal to b") if a==b else print("b is greater than a")    #output:  a is less than b

#6. And
#The and keyword is a logical operator, and is used to combine conditional statements:
#Example: Test if a is greater than b, AND if c is greater than a:
# a=220
# b=33
# c=550
# if a>b and a>c:
#     print("a is greater than both a and b")

#7. Or: The or keyword is a logical operator, and is used to combine conditional statements:
#Example: Test if a is greater than b, OR if a is greater than c:a = 200
# a=200
# b = 33
# c = 500
# if a>b or a>c:
#     print("Atleast one of the conditions is true")

#8. Not
#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

#Example: Test if a is NOT greater than b:
# a=33
# b=67
# if not a>b:
#     print("a is not gretaer than b")



#9. The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
# a=33
# b=40
# if a>b:
#     pass