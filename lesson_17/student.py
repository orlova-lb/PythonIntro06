
class Student:
    def __init__(self, name=None, age=None, grades=None):
        if not grades:
            self.__grades = []

        self.__name = name
        self.__age = age

    @property
    def name(self):
        # print('In property NAME')
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 <= age <= 100:
            self.__age = age
        else:
            self.__age = 25

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grade):
        self.__grades.append(grade)
