
class Group:
    def __init__(self, name, students=None):
        self.__name = name
        if not students:
            self.__students = []
        else:
            # self.__students = students.copy()
            for st in students:
                self.__students.append(st)

    def add_student(self, student):
        self.__students.append(student)

    def print_group(self):
        if not self.__students:
            print('Group is empty')
        else:
            for st in self.__students:
                print(st.name, '\t', st.age, '\t', st.grades)

    def get_students(self):
        return self.__students

    def get_name(self):
        return self.__name
