#
# a = []
# print(a, type(a))
#
# a = list()
# print(a, type(a))
#
# a = list('Hello World!')
# print(a, type(a))
#
# a = [1, 65, 23, 7, 3]
# print(a, type(a))
#
# a = [4, 't', True, 5.76]
# print(a, type(a))
#
# print(a[1])
# a[1] = 'Hello'
# print(a, type(a))
#
# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
#
# for element in a:
#     print(element, end=' ')
# print()
#
# """
#     split()
#     join()
# """
#
# s = 'D:/PROJECT/Python/HILLEL/PythonIntro06/lesson_06/lists.py'
# lst = s.split('/')
# print(lst)
#
# s1 = ' - '.join(lst)
# print(s1)

# a = [1, 2, 3, 4, 5, 6]
# print(a, id(a))
#
# b = a.copy()    # b = a
# print(b, id(b))
#
# a[2] = 'Hello'
# print(a)
# print(b)

from copy import deepcopy

a = [[1, 2, 3], [4, 5, 6]]
print(a[0][1])
b = deepcopy(a)     # b = a.copy()
print(a, id(a))
print(b, id(b))

a[0][1] = 'Hello'
print(a, id(a))
print(b, id(b))

"""
    x in A
    x not in A
    min(A)
    max(A)
    sum(A)
    
    A.index(x)      ValueError
    A.count(x)
    A.pop()
    A.pop(idx)
    A.append(x)
    A.insert(idx, x)
    A.clear()
    A.copy()
    A.extend(B)     ==>  A + B
    A.remove(x)     ValueError
    del A[idx]
    del A
    A.revers()
    A.sort()
"""
