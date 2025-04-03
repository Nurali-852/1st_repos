def generate(n):
    for x in range(n, 0, -1):
        yield x

n = int(input())
ob = generate(n)

for x in ob:
    print(x, end = " ")