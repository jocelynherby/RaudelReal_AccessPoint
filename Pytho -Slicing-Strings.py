b = 'hello, world!'
print(b[2:5])
#You can return a range of characters by using the slice syntax.Specify the start index and the end index, separated by a colon, to return a part of the string.

#the first character has index 0

b = 'hello, world!'
print(b[:5])
#not having a number for the start index, the range will automatically start with the first character.

b = 'hello, world!'
print(b[2:])
#and vise versa.

b = 'hello, world!'
print(b[-5:-2])
#using negitive indexing will make the slice start from the end.
