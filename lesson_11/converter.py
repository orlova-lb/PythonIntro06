# from string import ascii_uppercase


def converter_func(num, system):
    """
    :param num:
    :param system:
    :return:
    """
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # + ascii_uppercase # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    tmp = []
    while num > 0:
        r = num % system
        tmp.insert(0, s[r])
        num //= system

    # tmp.reverse()
    res = ''.join(tmp)

    return res


string = 'Hello World!'
number = 3498659784365984765
some_list = [3, 6, 'r', 3.14, True]


print('Module was load_1_4 lkjehgledkhf;dsk')


# print(__name__)
if __name__ == '__main__':
    # 11110001001000000
    print(converter_func(123456, 2))
