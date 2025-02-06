thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#NEXT is dobavlenie dvuh setov
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Mozhno i list
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)