from random import randint

lst = [randint(10, 90) for _ in range(35)]
print(lst)

# key = int(input("Please enter a number: "))
# for idx in range(len(lst)):
#     if lst[idx] == key:
#         print(idx)
#         break
# else:
#     print("Key not found!")


min_value = lst[0]
max_value = lst[0]
for el in lst:
    if min_value > el:
        min_value = el

    if max_value < el:
        max_value = el

print('max =', max_value)
print('min =', min_value)
