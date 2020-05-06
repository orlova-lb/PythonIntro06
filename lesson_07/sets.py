#
# x = set()
# print(x, type(x))
#
# s = 'D:/PROJECT/Python/HILLEL/PythonIntro06/lesson_07/sets.py'
# print(len(s))
# x = set(s)
# print(len(x))
# print(x)
#
# lst = []
# tup = ()
# print(lst)
# print(tup)
#
# s = {}
# print(s, type(s))
#
# a = {1, 2, 3}
# b = {1, 2, 3, 1}
# print(a)
# print(b)
# print(a == b)
from random import randint
a = {randint(10, 90) for _ in range(3)}
b = {randint(10, 90) for _ in range(5)}
print(a, len(a))
print(b, len(b))
# for element in a:
#     print(element, end=' ')

# A | B  ==> A.union(B)
# c = a | b
# print(c, len(c))
# c = a.union(b)
# print(c, len(c))

# A = A + B  => A += B
# a = a | b
# a |= b
# print(a)

# A & B  ==> A.intersection(B)
# c = a & b
# print(c)
# c = a.intersection(b)
# print(c)
# a &= b

# A - B  ==> A.difference(B)
# c = a - b
# print(c)
# a -= b

# A ^ B  ==> A.symmetric_difference(B)
# c = a ^ b
# print(c, len(c))
# a ^= b

# A <= B  ==> A.issubset(B)
# print(a <= b)
#
# # A >= B  ==> A.issuperset(B)
# print(a >= b)

# A.isdisjoint(B)
print(a.isdisjoint(b))

a = [randint(10, 90) for _ in range(10)]
print(a)
lst = list(set(a))
print(lst)
tup = tuple(b)
print(tup)

s = {'ertgrfwerq', 'y34wgrt2', 43534}
print(s)

s.add(435341)
print(s)

s.remove(43534)
print(s)

print(s.pop())
print(s)

s.clear()
print(s)

s = frozenset(('ertgrfwerq', 'y34wgrt2', 43534))
print(s)
