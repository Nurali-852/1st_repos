print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

#Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#Evaluate two variables:
x = "Hello"
y = 15

print(bool(type(x) == 'int'))
print(bool(y))

#The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
"""Cause its not empty and numbers does not equal 0"""

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
"""Cause they are empty"""

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #False

def myFunction() :
  return True

print(myFunction()) #will print: 'True'

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #YES!

#Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) #True