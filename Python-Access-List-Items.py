thisList = ['apple', 'banana', 'cherry']
print(thisList[1])
#the firstitem is 0

thisList = ['apple', 'banana', 'cherry']
print(thisList[-1])
#negitive index starts from the end

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[2:5])
#it will start at 2(it will be include) and end at 5(but it will not be included in it)

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[:4])
#the list starts at the first item becuase it has no start value

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[2:])
#the list starts at the second item, but finishes the list because there is end value

print(thisList[-4:-1])
#Specify negative indexes if you want to start the search from the end of the list

thisList = ['apple', 'banana', 'cherry']
if 'apple' in thisList:
  print('yes, "apple" is in the fruit list')
  #To determine if a specified item is present in a list use the in keyword
