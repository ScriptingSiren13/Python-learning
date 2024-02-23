# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# print("hello")  #hello
# print('hello')  #hello

#  b. Assign String to a Variable
# a='hello'
# print(a)    #hello

# c. Multiline Strings: You can assign a multiline string to a variable by using three quotes:
# d=""" Hello how are you? """
# print(d)  # Hello how are you?

# h=''' hello 
# how 
# are  you?

# '''
# print(h)


# d. Or three single quotes:
# c='''I am fine '''
# print(c)  #I am fine

#e. Strings are Arrays
# a="hello girls"
# print(a[1])  #h

# #f. Looping Through a String:
# for x in "banana":  
#     print(x)

#g. String Length: To get the length of a string, use the len() function.
# a="hello world"
# print(len(a))

#h. Check String: To check if a certain phrase or character is present in a string, we can use the keyword in.
# txt="The simplest thing in life will be the best."
# if "in" in txt:
#     print("'in' is in the txt")    #'in' is in the txt
# if "bring" not in txt:
#     print("'bring' is not in txt")   #'bring' is not in txt

#i. Slicing: You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
# b="Hello, coders!"
# print(b[3:7])  #lo, 

# - Slice From the Start:By leaving out the start index, the range will start at the first character:
# print(b[:7])   #Hello,

# #Slice To the End: By leaving out the end index, the range will go to the end:
# print(b[2:])   #llo, coders!

#j. Negative Indexing: Use negative indexes to start the slice from the end of the string:
# h="Hello coders!"
# print(h[-7:])  #coders!

#k. Python - Modify Strings:Python has a set of built-in methods that you can use on strings.
#- Upper Case:
# z="Hello, coders!"
# print(z.upper())   #HELLO, CODERS!

#-Lower Case:
# z="Hello, coders!"
# print(z.lower())   #hello, coders!

#-Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
# z="  Hello, coders!  "
# print(z.strip())  #Hello, coders!

#-Replace String:
# z="Hello, coders!"
# print(z.replace("c","r"))   #Hello, roders!

#-Split String: The split() method returns a list where the text between the specified separator becomes the list items.
# z="Hello, coders!"
# print(z.split(","))   #['Hello', ' coders!']
# print(z.split("o"))   #['Hell', ', c', 'ders!']

#l. String Concatenation: To concatenate, or combine, two strings you can use the + operator.
# a="hello"
# b="world"
# c=a + " " + b
# print(c)  #hello world

# i. String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# age=34
# txt="Hello I am a coder"+age
# print(txt)   #error

#m. But we can combine strings and numbers by using the format() method. The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
#ex 1:
# age=34
# txt="Hello I am a code of age {}"
# print(txt.format(age))

#ex. 2:  default order:
# items=50
# quantity=3
# price=100
# order=" I want {} bags of {} bottles each of rupees {}"   
# print(order.format(quantity, items,price))  # I want 3 bags of 50 bottles each of rupees 100

#positional formatting:
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# order=" I want {1} bags of {0} bottles each of rupees {2}"
# print(order.format(items, quantity,price))  # I want 3 bags of 50 bottles each of rupees 100

#keyword formatting:
# items=50
# quantity=3
# price=100
# order=" I want {quantity} bags of {items} bottles each of rupees {price}"
# print(order.format(quantity=quantity,items=items, price=price)) 
 
# Example 3: # Integers such as Binary, hexadecimal, etc., and floats can be rounded or displayed in the exponent form with the use of format specifiers. 
# string1="{0:b}".format(16)
# print(string1)   #10000

# string2="{0:e}".format(16)
# print(string2)   #1.600000e+01

# string3="{0:.2f}".format(1/8)
# print(string3)    #0.12
# string3="{0:.3f}".format(1/8)
# print(string3)   #0.125

# example 4: 
# string1="|{:<10}|{:^10}|{:>10}|".format('hey','coder','girls')
# print(string1)    #|hey       |  coder   |     girls|

# #or:

# string2="{0:<10} was founded in {1:>10}".format("GeeksforGeeks2",2009)
# print(string2)   #GeeksforGeeks2 was founded in       2009

#old style formatting:
#a.Float formatting:
#ex 1:
num=3.14159
# print("the float formatting of num is %f"%num)  #the float formatting of num is 3.141590
# print("the float formatting of num is %3.2f"%num)   #the float formatting of num is 3.14
# print("the float formatting of num is %3.4f"%num)   #the float formatting of num is 3.1416
#ex 2:
# integer1=45.9956
# print("formatting in 3.4f format:") #formatting in 3.4f format:
# print('the value of integer1 is %3.4f' %integer1)  #the value opf integer1 is 45.9956

# print("formatting in 3.2f format:")  #Formating in 3.2f format:
# print('the value of integer1 is %3.2f'%integer1)  #the value of integer1 is 46.00

# #b. Integer formatting :
# num=42.3
# print("the integer formatting of num is %d"% num)  #the integer formatting of num is 42

# #c. Exponent Formatting (%e):
# number= 123456
# print("The number in scientific notation is %e" %number)  #The number in scientific notation is 1.234560e+05

# d. Octal Formatting (%o):
# number=42
# print("The octal representation of 42 is %o "%number)  #The octal representation of 42 is 52 


#e. Hexadecimal Formatting (%x and %X):
# number=255
# print("the hexadecimal represntation of 255 is %x(lowercase)"%number) #the hexadecimal represntation of 255 is ff(lowercase)
# print("the hexadecimal represenatation of255 is %X(uppercase) "%number) #the hexadecimal represenatation of255 is FF(uppercase)

#f. Character Formatting (%c):
char='A'
print("The ASCII  value of %c is %d" %(char,ord(char)))  #The ASCII  value of A is 65
char1='Z'
print('The char1 %c has an ASCII value is of %d'%(char1,ord(char1)))   #The char1 Z has an ASCII value is of 90
#g. String formatting:
# name="alice"
# print("Hello, %s!"%name)  #Hello, alice!

# n. Escape Character: to insert characters that are illegal in a string, use an escape character.
# txt= "I love everything especially \"nature\", it is the best"
# print(txt)  #I love everything especially "nature", it is the best

#o. Reversing a Python String:
# h="hello coders!Welcome"

# print(h.join(reversed(h)))

# print(h[::-1])     #emocleW!sredoc olleh