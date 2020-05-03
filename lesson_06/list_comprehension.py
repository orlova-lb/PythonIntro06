
"""
    new_list = [ expression for item in list ]
    new_list = [ expression for item in list if conditional ]
"""
from random import randint

lst1 = [randint(10, 50) for _ in range(15)]
print(lst1)

lst2 = [value * 2 for value in lst1 if value % 2 == 0]
print(lst2)

s1 = [str(element) for element in lst2]
print(s1)

s2 = ' + '.join(s1)
print(s2)

s3 = ' - '.join(str(element) for element in lst2)
print(s3)
