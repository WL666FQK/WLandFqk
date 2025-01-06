# object是基类
class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def run(self):
        print('%s is running' % self.name)

    def eat(self):
        print('%s is eating' % self.name)

# 实例化，初始化一个对象时，调用__init__
xiaoming=Person('xiaoming',18,1.75)
xiaoming.run()
xiaoming.eat()
xiaomei=Person('xiaoming',17,1.65)
xiaomei.eat()
lili=xiaoming
print(id(lili))
print(id(xiaoming))