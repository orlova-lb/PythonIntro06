
# x = 5
#
# if x < 10:
#     print('Значение меньше 10')
# else:
#     print('Значение не меньше 10')
#
# PI = 3.15
#
# assert PI == 3.14, 'PI не равно 3.14'

import sys

print(sys.platform)

# assert 'linux' in sys.platform, 'Incorrect platform'


# assert 1 == 2, '1 not equal 2'

assert (1 == 2, '1 not equal 2')

print('Test after assert')
