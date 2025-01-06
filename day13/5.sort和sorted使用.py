# Author: 王璐
# Date: 2024/12/27
# Time: 14:20

def sort_str():
    l="This is a test string from Andrew".split()
    print(l)
    print(sorted(l,key=str.lower))

def sort_list_tuple():
    # Pycharm中竖选是shift+alt+鼠标左键
    student_tuples = [
        ('john','A',15),
        ('dave','B',12),
        ('jane','B',10),
    ]

    # lambda 就是匿名函数
    print(sorted(student_tuples,key=lambda i:i[0],reverse=True))

class Student:
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age

    def __repr__(self):  # 相对于str更加灵活
        return repr((self.name,self.grade,self.age))

# 排序的列表里是自定义的object
def sort_list_object():
    s=Student('john','A',15)
    print(s)

from operator import itemgetter,attrgetter

def use_operator():
    student_tuples=[
        ('john','A',15),
        ('dave','B',12),
        ('jane','B',10),
    ]
    print(sorted(student_tuples,key=itemgetter(2),reverse=True))
    student_objects = [
        Student('john','A',15),
        Student('jane','B',12),
        Student('dave','B',10),
    ]
    print(sorted(student_objects,key=attrgetter('age')))
    print(sorted(student_tuples,key=itemgetter(1,2))) # 先用年级排名，再按年龄
    print(sorted(student_objects,key=attrgetter('grade','age')))

def use_stability():
    l=[('red',1),('blue',1),('red',2),('blue',2)]
    l.sort(key=itemgetter(0))
    print(l)

if __name__ == '__main__':
    # sort_list_object()
    # use_operator()
    use_stability()