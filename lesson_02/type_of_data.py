"""
    int a = 9;
"""

count = 5
print(count)

count = 'Hello'
print(count)

d = count
print(d)


"""
        f|  |  |  |  |   char f;

                        | str     |
     count ------------>| ref = 2 |<----- d
                        | 'Hello' |
"""

"""
    числовой: int, float, complex
    строковый: str, ESCAPE, RAW, text
    булевый: bool (True, False)
    последовательности: list, tuple, range
    множества: set, frozenset
    словари (карты): dict
"""

print(4876578436578949486703850486504823658436589436508243650847654085659843 * 34876539487659832505676474083654085421356521432732654)
# 1.79E+308  =  1.79 * 10 ^ 308
# 2.23E-308  =  2.23 * 10 ^ -308

a = 3 ** 100000
print(a)
# b = a + 0.1
# print(b)

print(0.1 + 0.1 + 0.1)

num = input('Введите целое число: ')
print(num, type(num))
num = int(num)
print(num, type(num))


num = input('Введите вещественное число: ')
print(num, type(num))
num = float(num)
print(num, type(num))
