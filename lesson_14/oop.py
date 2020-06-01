

"""
1. наследование
2. полиморфизм
3. инкапсуляция
4. абстракция
"""

"""
class ClassName[(parent1, parent2 ... parentN)]:
    body of class
"""


class Point:
    """

    """
    name = 'Point name'

    def __init__(self, x=0, y=0):
        """

        :param x:
        :param y:
        """
        self.X = x
        self.Y = y

    def print_point(self):
        """
        """
        print('X =', self.X, 'Y =', self.Y)

    @staticmethod
    def func():
        print('Static method')


pt1 = Point()
pt2 = Point(4, 7)
pt3 = Point(9, 2)
print(id(pt1), type(pt1), pt1.X, pt1.Y, pt1.name)
print(id(pt2), type(pt2), pt2.X, pt2.Y, pt2.name)
print(id(pt3), type(pt3), pt3.X, pt3.Y, pt3.name)
Point.name = 'Test'
print(id(pt1), type(pt1), pt1.X, pt1.Y, pt1.name)
print(id(pt2), type(pt2), pt2.X, pt2.Y, pt2.name)
print(id(pt3), type(pt3), pt3.X, pt3.Y, pt3.name)

pt1.print_point()
pt2.print_point()
pt3.print_point()

Point.func()
pt1.func()


class SomeClass:
    pass


def square_method(self):
    return self.x ** 2


def init(self, x):
    self.x = x


print(SomeClass.__dict__)
SomeClass.new_attr = 45
SomeClass.init = init
SomeClass.square = square_method
print(SomeClass.__dict__)
obj = SomeClass()
obj.init(3)
print(obj.square())                             # 9
print(obj.new_attr)
print(obj.__dict__)
obj.SS = 'retwere'
print(obj.__dict__)


