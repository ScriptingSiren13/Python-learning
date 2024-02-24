#A set is a collection which is unordered, unchangeable*, and unindexed. 
#* Note: Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets.
#A set can contain different data types:


# fruits={"apple", "mango","grapes"}
# print(fruits)   #{'grapes', 'mango', 'apple'}

#2.Also, duplicates not allowed.True and 1 is considered the same value and False and 0 as well:
# set1={"apple","mango",True,1,2 , False, 0}
# print(set1)  #{False, True, 2, 'apple', 'mango'}

#3. Get the Length of a Set:To determine how many items a set has, use the len() function.
# print(len(set1))   #5

#4. type(): From Python's perspective, sets are defined as objects with the data type 'set':
#<class 'set'>

# print(type(set1))

#5. The set() Constructor: It is also possible to use the set() constructor to make a set.
# set2=set(("BMW", "G-WAGON", "SWIFT", "ECO SPORTS"))
# print(set2)    #{'ECO SPORTS', 'SWIFT', 'G-WAGON', 'BMW'}

#6. Access Items:
# You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

#7. Loop Items:
 # But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# set2=set(("BMW", "G-WAGON", "SWIFT", "ECO SPORTS"))
# for x in set2:
#     print(x)   #each element printed in different lines

# if "SWIFT" in set2:
#     print("yes swift is a car")

#8. Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

# set2.add("Scorpio")
# print(set2)   #{'SWIFT', 'Scorpio', 'BMW', 'ECO SPORTS', 'G-WAGON'}

#9. Add Sets
#  To add items from another set into the current set, use the update() method.
# set3={"Maruti Suzuki" ," Hyundai", "Tata"}
# set2.update(set3)
# print(set2)     #{'Tata', 'ECO SPORTS', 'SWIFT', ' Hyundai', 'Maruti Suzuki', 'BMW', 'G-WAGON'}

#10. Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)


#11. Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
#1. remove()
#Note: If the item to remove does not exist, remove() will raise an error.
# thisset = {"apple", "banana", "cherry","car"}
# thisset.remove("car")
# print(thisset)


#2. discard()
#Note: If the item to remove does not exist, discard() will NOT raise an error.
# thisset = {"apple", "banana", "cherry","car"}
# thisset.discard("car")
# print(thisset)

#3. pop()
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
# set4={"cabbage","carrot","cauliflower","cucumber"}
# set4.pop()
# print(set4)  #{'cabbage', 'cauliflower', 'carrot'}
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


#4. clear(): The clear() method empties the set:
# set4.clear()
# print(set4)   #set()


#5. del():The del keyword will delete the set completely:
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)   #error

#12. Join Two Sets:
#1.The union() :method returns a new set with all items from both sets:
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)   #makes entirely a new set
# print(set3)

#Keep ONLY the Duplicates: 
#1. The intersection_update(): method will keep only the items that are present in both sets.

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z=x.intersection_update(y)
# print(x)    #{'apple'}
# print(z)  #None



# 2. The intersection() method will return a new set, that only contains the items that are present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)    #{'apple'}
# print(x)    #{'apple', 'banana', 'cherry'}

#Keep All, But NOT the Duplicates
#1.  The symmetric_difference_update() : method will keep only the elements that are NOT present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)
# print(x)              # {'google', 'cherry', 'microsoft', 'banana'}

# 2.The symmetric_difference() :method will return a new set, that contains only the elements that are NOT present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)
# print(x)  #{'banana', 'cherry', 'apple'}
# print(z)   # {'banana', 'cherry', 'microsoft', 'google'}

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

