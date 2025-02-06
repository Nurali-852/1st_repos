x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #Через пробел
print(x + y + z) #Прямая конкатинация
x = 5
y = 10
print(x + y) #будет 15 потому что оба интеджеры
'''
Тут ошибка потому что нельзя плсануть разные типы данных
x = 5
y = "John"
print(x + y)
'''
#Но можно просто вывести через пробел
x = 5
y = "John"
print(x, y)

'''Чтобы создать global variable 
нужно создать снаружи функции,
либо внутри фунции указать с помощью слова global
'''
y = " YOOo"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x + y)