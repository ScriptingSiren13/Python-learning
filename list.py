# a.Create a List:
# thislist=["apple","mango","grapes"]
# print(thislist)
# list3=list(("hello","hi","bye"))
# print(list3)

# b. List items are ordered, changeable, and allow duplicate values:
# thislist=["apple","mango","grapes","apple"]
# print(thislist)

# c. List Length:
# #To determine how many items a list has, use the len() function:
# print(len(thislist))

#d. List Items - Data Types
# List items can be of any data type:
#A list can contain different data types:
# Example
# list1=["abc",37,True]
# print(list1)         #['abc', 37, True]
# print(type(list1))    #<class 'list'>

#e. Access Items:
#List items are indexed and you can access them by referring to the index number:
# thislist=["apple","mango","cherry"]
# print(thislist[0])
# print(thislist[-1])

#f.  The list() Constructor
# # It is also possible to use the list() constructor when creating a new list.
# list1=list(("apple","mango","banana"))
# print(list1)

# g. Range of Indexes:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])

#h. Check if Item Exists
# #To determine if a specified item is present in a list use the in keyword:

# if "apple" in thislist:
#     print("Yes apple is in this list")

#i. Change Item Value:
# thislist[1]="blackcurrant"
# print(thislist)

#j. Change a Range of Item Values:
# thislist[1:3]=["blackcurrent","watermelon"]
# print(thislist)


#-If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)    #['apple', 'watermelon']


#-If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# thislist=["apple","mango","banana"]
# thislist[1:2]=["blackcurrent","melon"]   
# print(thislist)  #['apple', 'blackcurrent', 'melon', 'banana']

#k.  Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# thislist=["apple","banana","mango"]
# thislist.insert(2,"watermelon")
# print(thislist)

# l. Append Items
# To add an item to the end of the list, use the append() method:
# thislist.append("orange")
# print(thislist)    #['apple', 'banana', 'watermelon', 'mango', 'orange']

# m. Extend List
# To append elements from another list to the current list, use the extend() method.
# fruits=["apple","mango","grapes"]
# veggies=["cabbage", "cauliflower"]
# fruits.extend(veggies)
# print(fruits)    #['apple', 'mango', 'grapes', 'cabbage', 'cauliflower']

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# list1=["apple","mango"]
# tuple1=["apple","mango"]
# list1.extend(tuple1)
# print(list1)   #['apple', 'mango', 'apple', 'mango']

#n. Python - Remove List Items

# Remove Specified Item
# The remove() method removes the specified item. If there are more than one item with the specified value, the remove() method removes the first occurance
# thislist = ["apple", "banana", "cherry", "orange","banana", "kiwi", "melon", "mango"]
# thislist.remove("banana")
# print(thislist)  #['apple', 'cherry', 'orange', 'banana', 'kiwi', 'melon', 'mango']

# o. Remove Specified Index
# The pop() method removes the specified index.
# thislist = ["apple", "banana", "cherry", "orange","banana", "kiwi", "melon", "mango"]
# thislist.pop(6)
# print(thislist)  #['apple', 'banana', 'cherry', 'orange', 'banana', 'kiwi', 'mango']

# The del keyword also removes the specified index:
# del thislist[2]
# print(thislist) #['apple', 'banana', 'orange', 'banana', 'kiwi', 'melon', 'mango']

#p. Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# thislist.clear()
# print(thislist)

# q. Loop Through a List
# You can loop through the list items by using a for loop:
# thislist = ["apple", "banana", "cherry", "orange","banana", "kiwi", "melon", "mango"]
# for x in thislist:
#     print(x)

# -A short hand for loop that will print all items in a list:
# thislist = ["apple", "banana", "cherry", "orange","banana", "kiwi", "melon", "mango"]
# [print(x) for x in thislist]

# r. Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

# thislist = ["apple", "banana", "cherry", "orange","banana", "kiwi", "melon", "mango"]
# for i in range(len(thislist)):
#     print(thislist[i])

# s. Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
# thislist = ["apple", "banana", "cherry", "orange","banana", "kiwi", "melon", "mango"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i+=1



