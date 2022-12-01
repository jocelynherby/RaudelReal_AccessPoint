thisList = ['apple', ' banana', 'cherry']
thisList.append('orange')
print(thisList)
#To add an item to the end of the list

thisList = ['apple', 'banana', 'cherry']
thisList.insert(1, 'orange')
print(thisList)

tropical = ['mango', 'pineapple', 'papaya']
thisList.extend(tropical)
print(thisList)
# to add another list to the current one use "extend()"

thisList = ['apple', 'banana', 'cherry']
thistuple = ('kiwi', 'orange')
thisList.extend(thistuple)
print(thisList)

