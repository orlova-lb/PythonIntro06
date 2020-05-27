from pprint import pprint as pp

lst = [
    'Максимальное напряжение, B              250',
    'Максимальный ток, А                     6',
    'Тип рабочего тока                       переменный',
    'Высота педали, мм                       43.5',
    'Толщина педали, мм                      18',
    'Количество контактов (без реверса)      6'
]

pp(lst)

file = open('example_file.txt', 'w', encoding='utf-8')
for line in lst:
    file.write(line)
    file.write('\n')

file.close()
print()

# read all
print()
lst = []
file = open('example_file.txt', encoding='utf-8')
lst = file.read()
file.close()
pp(lst)
print()

# read all
print()
lst = []
file = open('example_file.txt', encoding='utf-8')
lst = file.readlines()
file.close()
pp(list(map(lambda x: x.strip('\n'), lst)))
print()

# read by 40 symbols
lst = []
pp(lst)
file = open('example_file.txt', encoding='utf-8')
while True:
    line = file.readline(40)
    if line != '':
        lst.append(line.strip('\n'))
    else:
        break
file.close()
print()
pp(lst)

# read by line
lst = []
pp(lst)
file = open('example_file.txt', encoding='utf-8')
for line in file.readlines():
    lst.append(line.strip('\n'))
file.close()
print()
pp(lst)

# read by line
lst = []
pp(lst)
file = open('example_file.txt', encoding='utf-8')
for line in file:
    lst.append(line.strip('\n'))
file.close()
print()
pp(lst)
exit(0)
