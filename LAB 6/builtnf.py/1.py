import math

numbers = [2, 3, 4, 5]

from functools import reduce

result = reduce(lambda x, y: x * y, numbers)

print("Product of all numbers:", result)
