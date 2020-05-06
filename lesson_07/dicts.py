from pprint import pprint

# d = {}
# print(d, type(d))
#
# d = dict()
# print(d, type(d))
#
# d = {
#     'one': 1,
#     'two': 2,
#     'four': 4
# }
# print(d, type(d))
#
# d = dict(
#     [
#         ('one', 1),
#         ('two', 2),
#         ('four', 4)
#     ]
# )
# print(d, type(d))
#
# d = dict(
#     one=1,
#     two=2,
#     four=4,
# )
# print(d, type(d))
#
# print(d['two'])
#
# d = {
#     1: 'one',
#     2: 'two',
#     4: 'four'
# }
#
# print(d[2])
#
# d['five'] = 5
# print(d)
#
# d[5] = 'five'
# print(d)
#
# d[12] = 45
# print(d)
#
# del d[12]
# print(d)
#
# d[(3, 5)] = 56
# print(d)
#
# # d[[4, 5]] = 123
# # print(d)

person = {}
print(type(person))                             # <class 'dict'>
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
pprint(person)

print(person['fname'])
print(person['children'][1])
print(person['pets']['cat'])

print(person.get('age1', 25))

print(person.items())
for key, value in person.items():
    print(key, value)

print(person.keys())
print(person.values())

print(person.pop('age'))
pprint(person)

print(person.popitem())
pprint(person)

"""
    a = {}
    b = {}
    
    a.update(b)
"""

person.clear()
print(person)






























