#There are three numeric types in Python
x = 1  #int
y = 2.8  #float
z = 1j  #complex

print(type(x))
print(type(y))
print(type(z))

#integer is a whole number with infinate langth and does not have a decimal
x = 1
y = 364512476553564342157434
z = -38687386353

#a float number contains a one or more decimals, negative or positive
x = 1.10
y = 1.0
z = -35.59

#floats can also be a scientific number with an E to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#You can convert from one type to another with the int(), float(), and complex() methods
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#converting one type to another
#covert from int to float
a = float(x)

#convert from float in int
b = int(y)

#convert from in to complex 
c = complex(z)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#You cannot convert complex numbers into another number type.

#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers
import random

print(random.randrange(1, 10)) #prety cool RGN


