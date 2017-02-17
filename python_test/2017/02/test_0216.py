# coding:utf-8
import operator


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student('Luna', 10)
s2 = Student('Spe', 13)
s3 = Student('Lina', 16)

list_student = [s1, s2, s3]
cmp_ful = operator.attrgetter('age')  # 以此属性排序
print(cmp_ful)
list_student.sort(key=cmp_ful)
list_student = list_student[::-1]
for obj in list_student:
    print(obj.name, obj.age)
