# Your code here
import random
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

cache = {}
def slowfun(x, y):
    total = math.pow(x, y)
    if total not in cache:
        cache[total] = math.factorial(total)
        cache[total] //= (x + y)
        cache[total] %= 982451653
    total = cache[total]
    # print(total)
    return total
    

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
