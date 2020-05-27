from random import randint

lst = [[randint(-50, 150000) for _ in range(randint(1, 10))] for _ in range(10)]
print(lst)
print()

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print('|{a:5}'.format(a=lst[i][j]), end='')
    print('|')
print()

# res = '{}'.format(45)
# print(res)

