print(10 > 9)
print(10 == 9)
print(10 < 9)
#When you compare two values, the expression is evaluated and Python returns the Boolean answer

a = 200
b = 33

if b > a :
  print('b is greater than a')
else:
  print('be is not greater than a')
  #When you run a condition in an if statement, Python returns True or False

print(bool('hello'))
print(bool(15))

x = 'hello '
y = 15

print(bool(x))
print(bool(y))
#The "bool()" function allows you to evaluate any value, and give you True or False in return

bool('abc')
bool(123)
bool(['apple', 'charry', 'banana'])
#Any list, tuple, set, and dictionary are True, except empty ones, 0, and empty strings

bool(False)
#bool(none)
bool(0)
bool("")
bool(())
bool([])
bool({})
#these are the only values that evaluate back to false 

class myclass():
  def _len_(self):
    return 0 

myobj = myclass()
print(bool(myobj))
#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a "__len__" function that returns 0 or False

def myFunction():
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print('yes')
else:
  print('no')

x = 200
print(isinstance(x, int))
