# print(chr(0x26bd))
# print('\u26bd')
# print(chr(9917))
#
# print(ord('⚽'))
# print(hex(ord('⚽')))
#
# wave = '~'
# boat = '\U0001F6A3'
# seagull = '\u033C'
# fish = '\U0001F41F'
# penguin = '\U0001F427'
# wale = '\U0001F40B'
# octopus = '\U0001F419'
#
# row = wave * 10 + boat + wave * 15 + '\n'
# fish_row = wave * 4 + fish + wave * 21 + '\n'
# wale_row = wave * 10 + wale + wave * 15 + '\n'
# penguin_row = wave * 7 + penguin + wave * 18 + '\n'
# octopus_row = wave * 17 + octopus + wave * 8 + '\n'
#
# sea = row + fish_row + wale_row + penguin_row + octopus_row
# print(sea)

# a = """
# ;lsfdjhl;kfdjga
#     fdig
#
# sfdhkb'ofdj
# [dogjeragf'sda
# """
# print(a)

'''

'''

# s = 'Hello World!'
# # s = input('Please enter a string: ')
# l = len(s)
# print(l, s)
# print('Hello ' + 'World!')
# print('Hello ' * 5)

s = 'HELLO'
"""
            0  1  2  3  4  -> ERROR
            H  E  L  L  O
ERROR <-   -5 -4 -3 -2 -1
"""

print(s[1], s[-4])

"""
    slice
    
    str[start: stop: step]
"""
s = 'Python/HILLEL/PythonIntro06'
# print(s[0: 6])
# print(s[:6])
# print(s[7: 13])
# print(s[14: 9874908362089])
# print(s[14:])
# print(s[:])
# print(s[1::2])
# print(s[::-1])
#
# print(s[-20: -14])
#
# for i in range(len(s)):  # range(15)
#     if not i % 2:       # i % 2 == 0
#         print(s[i], end='')
# print()
#
# for symbol in s:
#     print(symbol, end='')
# print()

for i in range(0, len(s), -1):  # range(15)
    # if not i % 2:       # i % 2 == 0
    print(s[i], end='')
print()

"""
    methods
"""
s = 'Python/HILLEL/PythonIntro06'

idx = s.find('t')
print(idx)
idx = s.find('t', idx + 1)
print(idx)
idx = s.find('t', idx + 1)
print(idx)
idx = s.find('t', idx + 1)
print(idx)

idx = s.find('t')
while idx >= 0:
    print(idx)
    idx = s.find('t', idx+1)

print(s.replace('t', 'T'))

print(s.upper())
print(s.lower())
s = s.lower()
print(s.capitalize())

s = '      Python/HILLEL/PythonIntro06         '
print('"' + s.strip() + '"')
