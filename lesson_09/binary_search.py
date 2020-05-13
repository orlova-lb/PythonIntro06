from random import randint
from lesson_09.bubble_sort import bubble_sort


def binary_search(array, key, left=0, right=None):
    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key and left <= right:
        if array[middle] < key:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


lst = [randint(1, 100) for _ in range(35)]
print(lst)

bubble_sort(lst)
print(lst)

key = int(input("Please enter value: "))
is_found, idx = binary_search(lst, key)
if is_found:
    print('Index of key is:', idx)
else:
    lst.insert(idx, key)
    print(lst)


