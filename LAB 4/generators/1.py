class Myclass:
    def __init__(self, N):
        self.N = N
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < self.N:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
N = int(input())
myobject = Myclass(N)
myiter = iter(myobject)

for x in myiter:
    print(x * x)