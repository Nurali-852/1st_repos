"""Examples:"""
print(10 + 5) #"+" together to values

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))

#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3)

#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:
print(5 + 4 - 7 + 3)

#What will be the result of the following syntax:
x = 5
x += 3
print(x) #8

#Multiply 10 with 5, and print the result.
print(10*5)

#Divide 10 by 2, and print the result.
print(10/2)

#Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
 print("Yes, apple is a fruit!") #in

#Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
  print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true") #or