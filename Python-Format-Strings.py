age = 18
txt = 'my name is Raudel, and I am ' + age
print(txt)
 can't do that 

age = 18 
txt = 'my name is Raudel, and I am {}'
print(txt.format(age))
# using "format()" let us insert numbers into strings

quantity = 3
itemno  = 567
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars.'
print(myorder.format(quantity, itemno, price))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders

quantity = 3
itemno  = 567
price = 49.95
myorder = 'I want to pay {2} dollars for {0} pieces of item{1}.'
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
