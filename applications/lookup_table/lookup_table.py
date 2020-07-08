# Your code here
import random
import math

pows = {}
facts = {}
divs = {}
mods = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    p = (x, y)
    if p not in pows:
        pows[p] = math.pow(x, y)

    v = pows[p]
    if v not in facts:
        facts[v] = math.factorial(v)

    d = facts[v]
    if d not in divs:
        divs[d] = d // (x + y)

    m = divs[d]
    if m not in mods:
        mods[m] = m % 982451653

    return mods[m]
    

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
