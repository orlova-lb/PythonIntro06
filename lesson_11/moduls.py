
"""
    import <module_name>
    import <module_name> as <short_name>

    PYTHONPATH

    from <module_name> import <what>
    from <module_name> import <what> as <short_name>
"""

# import lesson_11.converter as c
# import lesson_11.converter as b

# from lesson_11.converter import converter_func, some_list, number
from lesson_11.converter import *

import random, time, sys

import sys

# print(sys.path)

#
print(converter_func(24332423, 2))
# print(c.some_list)
# print(b.string)

print(number)
print(some_list)

print(dir())
# print(__doc__)


def gen_list(size):
    from random import randint
    tmp = [randint(1, 100) for _ in range(size)]
    return tmp


