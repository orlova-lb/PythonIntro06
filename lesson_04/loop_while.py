"""
while <condition>:
    operator 1
    operator 2

    operator N
else:
    operator 1'
    operator 2'

    operator N'

operator K


"""

# num = int(input('Please enter positive number more than 0: '))
# if num <= 0:
#     print('Incorrect value!')
#     exit(1)
#
# i = 1
# while i <= num:
#     print(i, '** 2 =', i ** 2)
#     i += 1


"""
    break
"""

# while True:
#     num = int(input('Please enter positive number more than 0: '))
#     if num <= 0:
#         print('Incorrect value!')
#         print()
#     else:
#         break

"""
    определение количества цифр натурального числа n
"""

# num = int(input('Please enter positive number more than 0: '))
#
# amount = 0
# while num > 0:
#     num //= 10
#     amount += 1
#
# print('Amount of digit =', amount)

# while True:
#     print('first / second = result')
#     a = int(input('Please enter first number: '))
#     if a == 0:
#         print('Exit')
#         break
#
#     b = int(input('Please enter second number: '))
#     if b == 0:
#         print('Incorrect value\n')
#         continue
#
#     res = a / b
#     print('result =', res)
#     print()


a = int(input('Please enter a number: '))
while a != 0:
    if a < 0:
        print('Value is negative')
        break

    a = int(input('Please enter first number: '))
else:
    print('No any negative values')










