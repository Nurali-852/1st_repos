x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Which is NOT a legal numeric data type in Python: long

#Insert the correct syntax to convert x into a floating point number.

x = 5
x = float(x)
print(x)

#Insert the correct syntax to convert x into a integer.
x = 5.5
x = int(x)
print(x)

#Insert the correct syntax to convert x into a complex number.

x = 5
x = complex(x)
print(x)

#What will be the result of the following code:
print(int(35.88)) #35

print(float(35)) #35.0

print(str(35.82)) #35.82

#нету функции рандома. Но есть встроенный модуль который сможет сделать рандом
import random

print(random.randrange(1, 10))