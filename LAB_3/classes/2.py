class shape():
    def __init__(self):
        self.a = 0
    def area(self):
        print(self.a)
class square(shape):
    def __init__(self, length):
        self.length = length
        self.a = length ** 2

a = shape()
b = square(15)
a.area()
b.area()