from random import randint

# lst1 = [randint(10, 50) for _ in range(20)]
# print(lst1)
#
# lst2 = [element for element in lst1 if not element % 2]
# print(lst2)
#
# lst3 = [element if not element % 2 else element + 1 for element in lst1]
# print(lst3)


lst = [
    [23432421, 'uityroqeiutyqouitr', 5, 56.7],
    [78568734, 'gfhtrdfghtrgsfr', 2, 22.5],
    [87987656, 'uounytjtrgfrbgtrhtr', 1, 7.9],
    [12342353, 'ertyervrgregbgfrh', 6, 23.78],
]

# t = (4, 6, 7)
# t = 4, 6, 7


def func(el):
    s = el[2] * el[3]
    if s < 100:
        s += 10

    return el[0], s


res = list(map(lambda el: el[2] * el[3] if el[2] * el[3] >= 100 else el[2] * el[3] + 10, lst))
print(res)
