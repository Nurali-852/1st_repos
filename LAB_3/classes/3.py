class shape():
    def __init__(self):
        self.a = 0
    def area(self):
        print(self.a)
class rec(shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.a = (w + l)*2

a = shape()
c = rec(15, 78)

a.area()
c.area()