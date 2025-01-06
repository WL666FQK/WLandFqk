#9、练习私有属性和私有方法
class Person:
    def __init__(self,name):
        self.name=name
        self.__age=18

    def eat(self):
        self.__secret()

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name,self.__age))

women=Person("小美")
women.eat()

