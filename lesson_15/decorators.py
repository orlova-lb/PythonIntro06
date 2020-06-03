
def measure(value):
    from datetime import datetime
    print(value)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@measure('gen_1')
def gen_1(num):
    lst = []
    # start = datetime.now()
    for i in range(num):
        if i % 2 == 0:
            lst.append(i)
    # print(datetime.now() - start)

    return lst


@measure('gen_2')
def gen_2(num):
    # start = datetime.now()
    lst = [i for i in range(num) if i % 2 == 0]
    # print(datetime.now() - start)

    return lst


if __name__ == '__main__':
    lst1 = gen_1(10**6)
    print(len(lst1))
    lst2 = gen_2(10**6)
    print(len(lst2))

    # print(lst1)
    # print(lst2)

    # r = measure(gen_1)
    # print(r)
    # lst3 = r()
    # print(len(lst3))
    # # print(lst3)
    # for el in lst3:
    #     print(el)

    r_outer = measure('gen_1')
    print(r_outer)
    r_wrapper = r_outer(gen_1)
    print(r_wrapper)
    res = r_wrapper(100)
    print(res)
    print(len(res))

    res = measure('gen_1')(gen_1)(100)
    print(res)
    print(len(res))
