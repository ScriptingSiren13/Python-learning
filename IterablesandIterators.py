#DIFFERENCE BETWEEIterable:

# An iterable is an object that you can iterate over.
# It can be thought of as anything you can loop through or iterate item by item.
# Examples of iterables include lists, strings, tuples, and more.
# You can create an iterator from an iterable.
# Iterator:

# An iterator is an object that represents a stream of data.
# It maintains a state during iteration and remembers where it is in the sequence.
# You can obtain an iterator from an iterable by using the iter() function.
# The next() function is used to get the next item in the sequence from the iterator.


# #EXAMPLE 1:
# #iterable:list:
# lst=[1,2,3,4,5]

# #creating an iterator from iterable:
# my_iterator=iter(lst)

# #using iterator to get to the next item
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))


# #EXAMPLE 2:
# s="XYZ"
# y=iter(s)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))         #STOP ITERATION:because there is nothing more to print.
#WHY DO WE USE ITERATORS?
#If we convert list/iterable into an iterator, all the values will not be initilized in the memory .unless  we do not call an inbuilt function 'next', then only the first item that is present inside the iterator will be initialized in the memory.
#In case of an iterable, everything gets initiliazed inside the memory.


# #THE OTHER WAY TO DO IT:
# for i in y:
#     print (i)

#For loop does not give "Stop Iteration". It is because it has been already handled here.

#Iteration Process:

"""When you use a loop or the next() function to iterate over elements using an iterator, Python internally uses a special exception called StopIteration to signal when there are no more items to process.
End of Iteration:

Each time the loop or next() function is called, the iterator provides the next item in the sequence.
When there are no more items left, the iterator raises a StopIteration exception to indicate that the iteration has reached its end.
Handling StopIteration:

In most cases, you don't need to worry about StopIteration explicitly because Python handles it automatically behind the scenes.
When using a for loop, the loop recognizes the StopIteration exception and exits gracefully.
When using the next() function, you can catch StopIteration using a try and except block to handle the end of iteration.
Here's a simple example to illustrate the concept:  """

my_list = [1, 2, 3]

# Creating an iterator from the iterable
my_iterator = iter(my_list)

while True:
    try:
        print(next(my_iterator))
    
    except StopIteration:
        break
