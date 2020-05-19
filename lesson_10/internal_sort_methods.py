from random import randint
from pprint import pprint

text = """
    Василий Петров
    Андрей Говорухи
    Максим Мухин
    Кощей Бессмертный
    Гавриил Варфаломеев
    Спиридов Тереньтьев
    Маргарита Мартынова
    Илья Муромцев
    Станислав Трердолобов
    Полина Гусева
    Петр Николаев
    Игнат Тюльпанов
"""


def mprint(lst, variant):
    template_1 = '{full_name:<30}{grades}'
    template_2 = '{full_name:<30}{grades}{summa:>4}'
    template_3 = '{full_name:<30}{grades}{summa:>4}{avg:>6}'
    grades = '{grade:<3}'

    for line in lst:
        lst = line.split(', ')

        if variant == 1:
            print(template_1.format(
                full_name=lst[0],
                grades=''.join(grades.format(grade=x) for x in lst[1:]),
            ))
        elif variant == 2:
            print(template_2.format(
                full_name=lst[0],
                grades=''.join(grades.format(grade=x) for x in lst[1:-1]),
                summa=lst[-1]
            ))
        elif variant == 3:
            print(template_3.format(
                full_name=lst[0],
                grades=''.join(grades.format(grade=x) for x in lst[1:-2]),
                summa=lst[-2],
                avg=lst[-1]
            ))
        else:
            pprint(lst)


def get_surname(full_name):
    return full_name.split()[1]


# преобразуем многострочный текст в список
names = [name.strip() for name in text.strip('\n').split('\n')]
pprint(names)
print()

# сортируем по фамилии
names.sort(key=get_surname)
pprint(names)
print()

# а теперь сортируем по имени
names.sort(key=lambda full_name: full_name.split()[0])
pprint(names)
print()

# добавляем каждому ученику по 12 оценок
rating = [name + ', ' + ', '.join([str(randint(1, 10)) for _ in range(12)]) for name in names]
mprint(rating, 1)
print()

# вычисляем и добавляем каждому ученику сумму оценок
rating = [line + ', ' + str(sum(int(x) for x in line.split(', ')[1:])) for line in rating]
mprint(rating, 2)
print()

# вычисляем и добавляем каждому ученику средний балл
rating = [line + ', ' + str(round(int(line.split(', ')[-1]) / len(line.split(', ')[1:-1]), 2)) for line in rating]
mprint(rating, 3)
print()

# сортируем по сумме оценок
rating.sort(key=lambda element: sum(int(value) for value in element.split(', ')[1:-2]))
mprint(rating, 3)
print()

# сортируем по среднему баллу
rating.sort(key=lambda element: round(
    sum(int(value) for value in element.split(', ')[1:-2])/len(element.split(', ')[1:-2]), 2))
mprint(rating, 3)
print()

# используем для сортировки метод sorted()
n = sorted(names, key=lambda full_name: full_name.split()[0])
pprint(n)
print()

# сортируем по длине имени
n = sorted(names, key=lambda full_name: len(full_name.split()[0]))
pprint(n)
print()

# сортируем по имени в обратном порядке
n = sorted(names, key=lambda full_name: full_name.split()[0], reverse=True)
pprint(n)
print()
