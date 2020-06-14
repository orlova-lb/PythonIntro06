from student import Student
from group import Group


name = input('Please enter group name: ')
gr = Group(name)

cnt = int(input('Please enter count of studens: '))
for i in range(cnt):
    st = Student()
    st.name = input('Please enter name: ')
    st.age = int(input('Please enter age: '))
    cnt_g = int(input('Please enter count grades: '))
    for j in range(cnt_g):
        grade = int(input('Please enter grade {}: '.format(j+1)))
        st.grades = grade

    gr.add_student(st)


print('Group:', gr.get_name())
for st in gr.get_students():
    print(
        'Name:', st.name,
        '\tAge:', st.age, '\tGrades:',
        round(sum(st.grades)/len(st.grades), 2)
    )





# def t(a, lst=None):
#     if not lst:
#         lst = []
#     lst.append(a)
#     print(lst)
#
#
# t(4)
# t(6)

