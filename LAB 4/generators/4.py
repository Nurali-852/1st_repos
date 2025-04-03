def generate(a, b):
    for x in range(a, b):
        yield x*x

a = int(input())
b = int(input())
ob = generate(a, b)

for x in ob:
    print(x)