"""
for <value> in <iterable_obj>:
    operator 1
    operator 2

    operator N

for <value> in <collection>:
    operator 1
    operator 2

    operator N

for _ in <iterable_obj>:
    operator 1
    operator 2

    operator N
"""

# print('Hello', 'World!', sep=' --- ')
# exit(0)


# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print('#', i, ' color of rainbow is ', color, sep='')
#     i += 1

# for i in 1, 2, 3.7, 'one', 'two', True, 'three':
#     print(i)


# for symbol in 'D:/PROJECT/Python/HILLEL/PythonIntro06/lesson_04/loop_for.py':
#     print(symbol, end=' ')
# print()

"""
    range(start, stop, step)
    
    range(stop)
"""

# range(1, 10, 2)
# range(10)

for i in range(1, 10, 2):
    print(i)

print()
for i in range(10):
    print(i)

print()
for _ in range(10):
    print('A')
