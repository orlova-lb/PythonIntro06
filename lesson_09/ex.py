
"""
    Найти произведение элементов списка, кратных 6 и оканчивающихся на 8. Если таких элементов нет - сообщить об этом.
"""

from random import randint

lst = [randint(1, 100) for _ in range(35)]
print(lst)


def search(collection):
    tmp = []
    p = 1
    for el in collection:
        if el % 6 == 0 and el % 10 == 8:
            tmp.append(el)
            p *= el

    tmp.insert(0, p)

    return tmp


if __name__ == '__main__':
    res = search(lst)
    if len(res) == 1:
        print('Value not found')
        exit(0)

    print(' * '.join([str(x) for x in res[1:]]) + ' = ' + str(res[0]))
