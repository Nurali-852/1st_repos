#What will be the result of the following code:
x = 'Welcome'
print(x[3]) #c

x = "Hello World"
print(len(x)) #длина строки ввиде цифры

txt = "Hello World"
x = txt[0] #Нужно получить первый знак тхт
print(x)

#чекаем есть ли фри в тексте
txt = 'The best things in life are free!'
if 'free' in txt:
  print('Yes, free is present in the text.')

#What will be the result of the following code:
x = 'Welcome'
print(x[3:5]) #co

#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
print(x)

#What will be the result of the following code:
x = 'Welcome'
print(x[3:]) #come

#What is a correct syntax to print a string in upper case letters?
print('Welcome'.upper())

#Return the string without any whitespace at the beginning or the end.
txt = " Hello World"
x = txt.strip()
print(x)

#Convert the value of txt to lower case.
print("HELLO, WORLD!".lower())

#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)

#What is a correct syntax to merge variable x and y into variable z?
x = "KOKO"
y = " JAMBO"
z = x + y
print(z)

#What will be the result of the following code:
x = 'Welcome'
y = 'Coders'
print(x + y) #WelcomeCoders

#What is a correct syntax to print 'Join the party'?
a = 'Join'
b = 'the'
c = 'party'
print(a + " " + b + " " + c)

#If x = 9, what is a correct syntax to print 'The price is 9.00 dollars'?
x = 9
print(f'The price is {x:.2f} dollars')

#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = f"My name is John, and I am {age}"
print(txt)

#What will be the result of the following code:
print(f'The price is {2 + 3} dollars') #The price is 5 dollars