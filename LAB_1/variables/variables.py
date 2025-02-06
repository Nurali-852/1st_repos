x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # Можно сразу давать значение в тот момент и создаеться. И мы не обьязаны уточнять тип переменной

#Casting уточнение типа переменной:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#type() выводит тип выбранной переменной
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A не изменит a

#правильные названия
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''неправильные
2myvar = "John"
my-var = "John"
my var = "John"'''