fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#loop string:
for x in "banana":
  print(x)


#break:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#Exit the loop when x is "banana", reak comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#continue:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)



#start at 2
for x in range(2, 6):
  print(x)



#with increment 3
for x in range(2, 30, 3):
  print(x)

#else:
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#if loop executed by break, else doesn't work
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested loop:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



# pass:
for x in [0, 10, 2, 8, 8, 16]:
  if(x == 0 or x == 8):
    pass
  else:
    print(x)