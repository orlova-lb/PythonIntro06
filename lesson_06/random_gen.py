
import random

from random import randint
# from random import random
from random import randrange
from random import uniform

# randrange
for _ in range(15):
    print(randrange(1, 10, 1), end=', ')
print()

for _ in range(15):
    print(random.randrange(1, 10, 1), end=', ')
print()

# randint
for _ in range(15):
    print(randint(1, 10), end=', ')
print()

# random
# for _ in range(15):
#     print(random(), end=', ')
# print()

# uniform
for _ in range(15):
    print(round(uniform(0.1, 9.9), 2), end=', ')
print()
