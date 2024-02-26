#1. Simple generator:
#Ex 1:
# def simpleGernerator():
#     yield 1
#     yield 2
#     yield 3

# for x in simpleGernerator():
#     print(x)
#Output:
#1
#2
#3
    
#Ex 2:
# def my_generator():
#     for x in range(10):
#         yield x
# gen=my_generator()
# print(next(gen))  #0
# print(next(gen))  #1
# print(next(gen))  #2
# for j in gen:
#     print(j)    #will print from 0-10

#2. Comparison of the generators and list:
# EX 1: Square of numbers:
# def square_numbers(nums):
#     result=[]
#     for i in nums:
#         result.append(i*i)
#     return result
# my_nums=square_numbers([1,2,4,5,8])
# print (my_nums)   #[1, 4, 16, 25, 64]

#3. NOW DOING THE SAME IWTH THE GENERATORS:
# def square_number(nums):
#     for i in nums:
#         yield(i*i)

# my_nums=square_number([2,4,6,8])
# print(next(my_nums))  #4
# print(next(my_nums))  #16
# print(next(my_nums))  #36

# #For priting the entire sequence:
# for i in my_nums:
#     print(i)

#Output: 
# 4
# 16
# 36
# 64

#Example2 :
# import sys

#  Generator function
# def my_generator(n):
#     for i in range(n):
#         yield i

# #Using a generator
# gen = my_generator(1000)
# print(sys.getsizeof(gen))  # Size of the generator object

# #Using a list
# lst = [i for i in range(1000)]
# print(sys.getsizeof(lst))  # Size of the list object

#Example 3:
# A simple generator for Fibonacci Numbers 
def fib(limit): 
	
	# Initialize first two Fibonacci Numbers 
	a, b = 0, 1

	# One by one yield next Fibonacci Number 
	while a < limit: 
		yield a 
		a, b = b, a + b 

# Create a generator object 
x = fib(5) 

# Iterating over the generator object using next 
# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 

# Iterating over the generator object using for 
# in loop. 
print("\nUsing for in loop") 
for i in fib(5): 
	print(i)  
#Output:
# 0
# 1
# 1
# 2
# 3
# 10
# 12
# 14
# 16
# 18

#4. Python Generator Expression:
#Ex 1:

# generator_exp=(i*5 for i in range(10) if i%2==0)
# for i in generator_exp:
#     print(i)
 #Output:
# 0
# 10
# 20
# 30
# 40

#Ex 2: 
generator_exp=(x+10 for x in range(10) if x%2==0)

for x in generator_exp:
    print(x)

#Output