class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Position: (x, y) = {self.x, self.y}")
    def move(self, x2, y2):
        self.x += x2
        self.y += y2
    def dist(self, x2, y2):
        return ((self.x - x2)**2 + (self.y - y2)**2)**(1/2)

a = point(1, 1)
a.show()

a.move(-15, +60)
a.show

d = a.dist(0, 0)
print(f"Distance =", int(d))