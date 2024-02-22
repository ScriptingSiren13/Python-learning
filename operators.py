
# -Operators are used to perform operations on variables and values.
# -Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# a. Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
# x=8
# y=7
# print(x+y) #15
# print(x-y) #1
# print(x*y)  #56
# print(x/y)  #full quotient 1.142
# print(x%y)  #remainder is 1
# print(x**y)  #2097152
# print(x//y)  #1 =The floor division operator ( // ) is primarily used when you require an integer or need to return the smallest integer less than or equal to the input. If the operands are both integers, then the output will an integer. If either operand is a float then the output will be a float.


# b. Python Assignment Operators
# Assignment operators are used to assign values to variables:
# x=y=z=a=b=c=d=e=f=g=h=i=5
# x+=3  #8
# y-=1  #4
# z*=3  #15
# a/=3  #1.666
# b%=3  #2
# c//=3 #1
# d**=3   #125
# e&=3  #1
# f|=3 #7
# g^=4 #XOR- 1
# h>>=3  #right shift 0
# i<<=3 #left shift 40
# print(x,y,z,a,b,c,d,e,f,g,h,i)

# c. Python Comparison Operators
# Comparison operators are used to compare two values
# x=6
# y=2
# print(x==y)  #false
# print(x!=y)  #true
# print(x>y)   #true
# print(x<y)
# print(x>=y)
# print(x<=y)

# d. python logical operators:

# x=10
# if x>20 and x<20:
#     print("x is between 20-30")

# if x>20 or x>5:
#     print("x is greater than 10")

# if not(x>20):
#     print("x is not greater than 0")
#Order of Precedence of Logical Operators:
    
# def order(x):
#     print("method called for values",+ x)
#     return True if x>0 else False
# a=order
# b=order
# c=order

# if a(-1) or b(5) or c(7):
#     print("At least one of them is positive")
 
# e. Membership operators:
# 1. in:
# list1=[2,3,4,5,6]
# list2=[2,3,4,5,9]
# for i in list1:
#     if i in list2:
#         print("overlapping")
#     else:
#         print("not overlapping")
# #o/p:
#overlapping
#overlapping
#overlapping
#overlapping
        
#2. not in:
# x=2
# y=4
# list=[2,4,87]
# if x not in list:
#     print("x not in list")
# elif y not in list:
#     print("y is not in list as well")
# elif x and y not in list:
#     print("both x and y are not in list")
# else:
#     print("both x and y are in list")

# f. Identity operators:
# -is
# x=7
# y=7
# print(id(x))
# print(id(y))
# if id(x) is id(y):
#     print(True)
# else:
#     print(False)

#is not:
# x=["Hello", "my", "dear"]
# y=["Hello", "my", "dear"]
# z=x

# print(x is not z)  #false
# print(x is not y)  #true
# print(x!=y)        #false

# g. Bitwise operator:
print(6 & 8)  #0
print(6|3)    #7
print(6^3)    #5
print(~3)     #-4
print(3<<2)   #12
print(8>>2)   #2