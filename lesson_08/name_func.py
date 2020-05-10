"""
def <name_function>([param1, param2, .... paramN]):
    body_of_function
"""


# def hello():
#     print('Hello World!')
#
#
# hello()


# def some_func():
#     pass
#
#
# def draw_rect(rows, cols):
#     for _ in range(rows):
#         for _ in range(cols):
#             print('*  ', end='')
#         print()
#     print()


# a = 4
# b = 6

# draw_rect(a+b, b)


# def my_pow(base, exp=2):
#     print(base ** exp)


# my_pow(4, 5)
# my_pow(5)


# def func(a, b, c=1, d=2, e=3):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
#     print()
#
#
# func(0, 0)
# func(0, 0, 11)
# func(0, 0, 11, 12)
# func(0, 0, 11, 12, 13)


def func(x):
    print(x)
    y = 6
    print(y)


z = 90


# def func1():
#     global z
#     z = 50
#     print(z)        # 1
#
#
# print(z)            # 2
# func1()
# print(z)            # 3


# def func(a, b, c, d=1, e=2, f=3):
#     print('a = {A}\tb = {B}\tc = {C}\td = {D}\te = {E}\tf = {F}\n'.format(
#         A=a, B=b, C=c, D=d, E=e, F=f
#     ))
#
#
# func(10, 20, 30)
# func(e=200, a=10, f=300, c=30, b=20)
# func(10, 20, 30, f=300, d=100)


# def func(a, b=[]):
#     print('before b =', b, end='\t')
#     b.append(a)
#     print('after append b =', b)
#
#
# s = []
# func(1, s)
# func(1)
# func(2)
# func(3)


# def func1(a, b=None):
#     print('before b =', b, end='\t')
#     if b is None:
#         b = []
#     b.append(a)
#     print('after append b =', b)
#
#
# s = []
# func1(1, s)
# func1(1)
# func1(2)
# func1(3)

# print(1, 2, 3, 4, 5, 6)

"""
    *args       **kwargs
"""


# def func(*args):
#     print(args, type(args))
#     for i in args:
#         print(i, end=' ')
#     print()
#
#
# func(3, 6, 'rt', 6.34, True, 5+7)


# def func(**kwargs):
#     print(kwargs, type(kwargs))
#
#
# func(e=200, a=10, f=300, c=30, b=20)


def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


# print(compare(2, 5))
# x = compare
# print(x(2, 5))


# def my_sort(lst, comp):
#     for i in range(len(lst)-1):
#         print(comp(lst[i], lst[i+1]))
#
#
# from random import randint
# l = [randint(10, 90) for _ in range(15)]
# print(l)
# my_sort(l, compare)


a = 90, 56, 67


def basic_arithmetic(x, y):
    suma = x + y
    product = x * y
    quotient = x / y
    difference = x - y

    return suma, product, quotient, difference


res = basic_arithmetic(8, 2)
print(res, type(res))
a, b, c, d = res
print(a, b, c, d)
