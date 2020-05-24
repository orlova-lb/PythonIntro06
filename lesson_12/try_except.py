"""
    try:
        operation
    except <Type_Of_Error>:
        action

"""


# a = int(input('Please enter A: '))
# b = int(input('Please enter B: '))

# if b != 0:
#     print('A / B =', a / b)
# else:
#     print('B is Zero.')
# while True:
#     try:
#         a = int(input('Please enter A: '))
#         b = int(input('Please enter B: '))
#
#         print('A / B =', a / b)
#         print('After division')
#     # except Exception as ex:
#     #     print('Exception', ex)
#     except ZeroDivisionError as ex:
#         print('Except message:', ex)
#     except ValueError as ex:
#         print('Except message:', ex)
#     else:
#         print('No error!')
#     finally:
#         print('Block finally')
#
#     print('After try.')


# print('After try.')

# from random import randint
#
# lst = [randint(10, 50) for _ in range(5)]
# for el in lst:
#     pass
#
# it = iter(lst)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))

def division(a, b):
    if b == 0:
        raise ZeroDivisionError('Incorrect value')

    return a / b


x = 9
y = 0
try:
    print(division(x, y))
except ZeroDivisionError as ex:
    pass
