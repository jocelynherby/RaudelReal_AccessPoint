print('hello, world')
print("hello, world")

#assigning string to a variable
a = 'hello'
print(a)

#multiline string by using three quotes
a = """leron idfum dolor sit amet 
consenctrrtit sadiujuewfbdjv elisfe, iorehgiuwby4jb
i uvuiugrwjdufewk fbu nde feueu u"""
print(a)
a = '''leron idfum dolor sit amet 
consenctrrtit sadiujuewfbdjv elisfe, iorehgiuwby4jb
i uvuiugrwjdufewk fbu nde feueu u'''
print(a)
#in the result, the line breaks are inserted at the same position as in the code (i dont really unnderstand what this means)

a = ('hello, world')
print(a[1])
#strings in Python are arrays of bytes representing unicode characters.

for x in 'banana' :
  print(x)
  #Since strings are arrays, we can loop through the characters in a string, with a for loop

a ='hello, world'
print(len(a))
#we find out the length of a string with "len()"

txt = 'the best things in life are free'
print('free' in txt)
txt = 'the best things in life are free'
if 'free'in txt:
  print('yes "free" is present.')#i dont totally get this part
#To check if a certain phrase or character is present in a string, we can use the keyword "in" 

txt = 'the best things in life are free'
print('expensive=' not in txt)
txt = 'the best things in life are free'
if 'expensive' not in txt:
  print('no, "expensive" is NOT present')
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
