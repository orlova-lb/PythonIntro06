"""
    2 ^ 4 ==> 2 * 2 * 2 * 2
    2 ^ 4 ==> 2 * 2^3 ==> 2 * 2^2 ==> 2 * 2^1 ==> 2 * 2^0 == 1
      16      2 * 8       2 * 4       2 * 2       2 * 1
"""


def i_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1

    return res


def r_pow(num, exp):
    if exp == 0:
        return 1

    return num * r_pow(num, exp-1)


print(i_pow(2, 4))
print(r_pow(2, 4))


"""
    0  1  2  3  4  5  6  7  8  9 10 11
    0  1  1  2  3  5  8 13 21 34 55 89
"""


def i_fib(n):
    n1 = 0
    n2 = 1

    while n > 1:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1

    return n3


def r_fib(n):
    if 0 <= n <= 1:
        return n

    return r_fib(n-1) + r_fib(n-2)


print(i_fib(10))
print(r_fib(4))

# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1000000)
# print(sys.getrecursionlimit())
