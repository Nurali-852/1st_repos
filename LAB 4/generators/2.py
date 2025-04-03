def gener(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = int(input())
g = gener(n)

for i in g:
    print(str(i) + ",", end = " ")