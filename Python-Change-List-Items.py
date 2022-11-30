thisList = ['apple', 'banana', 'cherry']
thisList[1] = 'blackcurrent'
print(thisList)
#changing a value of specific item

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
thisList[1:3] = {'blackcurrent', 'watermelon'}
print(thisList)
#

thisList = ['apple', 'banana', 'cherry']
thisList[1:2] = ['blackcurrent', 'watermelon']
print(thisList)
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

thisList = ['apple', 'banana', 'cherry']
thisList[1:3] = ['watermelon']
print(thisList)
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

thisList = ['apple', 'banana', 'cherry']
thisList.insert(2, 'watermelon')
print(thisList)
#The "insert()" method inserts an item at the specified index

