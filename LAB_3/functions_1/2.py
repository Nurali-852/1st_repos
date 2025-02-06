def to_celcium(f):
    return (f - 32) * (5 / 9)

print(f"Input in F:")
f = int(input())
c = to_celcium(f)
print(c)


