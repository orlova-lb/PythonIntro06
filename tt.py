import os
from time import sleep

h = int(input('Please enter height: '))
# l = int(input('Please enter level: '))

for l in range(h // 2):
    os.system('cls')
    for i in range(h):
        for j in range(h):
            if (
                    i == 0
                    or i == h - 1
                    or i == j
                    or j == h - i - 1
                    or (j == h // 2 and i > h // 2)
                    or (l < i < h // 2 and i <= j <= h - i - 1)
                    or (h - (l + 2) < i < h - 1 and h - 1 - i <= j <= i)
            ):
                print('* ', end='')
            else:
                print('  ', end='')
        print()
    sleep(1)
