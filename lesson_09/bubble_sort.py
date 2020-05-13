
from random import randint


def bubble_sort(my_lst):
    count_of_iteration = 0
    for i in range(len(my_lst) - 1):
        flag = True
        for j in range(len(my_lst) - 1 - i):
            if my_lst[j] > my_lst[j + 1]:
                my_lst[j], my_lst[j + 1] = my_lst[j+1], my_lst[j]
                flag = False
        count_of_iteration += 1
        if flag:
            break

    print(count_of_iteration)


if __name__ == '__main__':
    lst = [randint(1, 100) for _ in range(35)]
    print(lst)
    bubble_sort(lst)
    print(lst)

# 35
