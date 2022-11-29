myList = ['apple', 'banana', 'cherry']

thisList = ['apple', 'banana', 'cherry']
print(thisList)
#lists are odered, in that when you add a new item it will be places ar the end of a list
#:There are some list methods that will change the order, but in general: the order of the items will not change

thisList = ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(thisList)

thisList = ['apple', 'banana', 'cherry']
print(len(thisList))
#to see how many items are in the lists

list1 = ['apple', 'banana', 'cherry']
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#items can be any data type

list1 = ['abc', 34, True, 40, "male"]
print(list1)
#a list can aslo contain diffrent data types

myList = ['apple', 'banana', 'cherry']
print(type(myList))
#lists are classifed as "list" type in python

thisList = list(('apple', 'banana', 'cherry')) # note the double round brackets
print(thisList)

# Set items are unchangeable, but you can remove and/or add items whenever you like.
