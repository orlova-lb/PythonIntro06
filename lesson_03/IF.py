"""
if <condition>:
    operator 1
    operator 2
else:
    operator 4
    operator 5

operator 3
"""

# x = 3
# if x == 0:
#     print('x is zero')
# else:
#     print('x is not zero')

"""
    x = 6
"""

x = -4
if x > 0:
    print('x is positive')
elif x < 0:
    print('x is negative')
else:
    print('x is zero')


"""
    A ? B : C
    B if A else C
"""

x = 8
a = (4 if x != 5 else x)
print(a)
