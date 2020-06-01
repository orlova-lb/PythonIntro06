"""
    |345612|
"""


#   1   2345 * 10 = 23450 + 1 = 23451
def shift_left(number):
    tmp = number
    d = 0
    amount = 0
    while tmp > 0:
        d = tmp % 10
        tmp //= 10
        amount += 1

    number = number % (10 ** (amount - 1)) * 10 + d

    return number


# 1234   5  ==>  51234  ==>  5 * 10000 = 50000 + 1234 = 51234
def shift_right(number):
    tmp = number
    d = tmp % 10
    tmp //= 10
    multi = 1
    while tmp > 0:
        multi *= 10
        tmp //= 10

    number = d * multi + number // 10

    return number


def shift(number, step, direction=False):
    for _ in range(step):
        if direction:
            number = shift_right(number)
        else:
            number = shift_left(number)

    return number


num = 12345678
num = shift(num, 5)
print(num)
print(shift(num, 5, True))
