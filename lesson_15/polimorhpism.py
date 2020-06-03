class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__a = age  # устанавливаем возраст

    @property
    def name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__a

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__a = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__a)


class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    # переопределение метода display_info
    def display_info(self):
        super().display_info()
        print("Компания:", self.company)


class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)


person = Person("Tom", 23)
person.display_info()
person.set_name('Bob')
person.display_info()
person.age = 29
person.display_info()
print(person.age)





# people = [Person("Tom", 23), Student("Bob", 19, "Harvard"), Employee("Sam", 35, "Google")]
#
# for person in people:
#     person.display_info()
#     print()