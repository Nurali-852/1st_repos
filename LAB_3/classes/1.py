class stringsters():
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

x = stringsters()
x.getString()
x.printString()