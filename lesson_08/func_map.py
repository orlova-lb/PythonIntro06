def fahrenheit(temperature):
    return round(((float(9)/5)*temperature + 32), 2)


def celsius(temperature):
    return round((float(5)/9)*(temperature-32), 2)


# temperatures = [36.5, 37, 37.5, 38, 39]
# l = []
# for t in temperatures:
#     l.append(fahrenheit(t))
# print(l)
#
# print(map(fahrenheit, temperatures))
#
# temperatures_in_fahrenheit = list(map(fahrenheit, temperatures))
# temperatures_in_celsius = list(map(celsius, temperatures_in_fahrenheit))
# print(temperatures_in_fahrenheit)               # [97.7, 98.6, 99.5, 100.4, 102.2]
# print(temperatures_in_celsius)


C = [39.2, 36.5, 37.3, 38, 37.8]

F = list(map(lambda x: round((float(9)/5)*x + 32, 2), C))
print(F)                                        # [102.56, 97.7, 99.14, 100.4, 100.04]

C = list(map(lambda x: round((float(5)/9)*(x-32), 2), F))
print(C)