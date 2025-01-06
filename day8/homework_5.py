# 5、设计一个类，实例化两个对象，然后小明跑步跑完步，会去吃东西
# ，小美不跑步，小美喜欢吃东西
# • 小明 今年 18 岁，身高 1.75，每天早上 跑 完步，会去 吃 东西
# • 小美 今年 17 岁，身高 1.65，小美不跑步，小美喜欢 吃 东西
class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def run(self):
        print("%s 跑步" % self.name)

    def eat(self):
        print("%s 吃东西" % self.name)

xiaoming=Person("小明",18,1.75)
xiaoming.run()
xiaoming.eat()
xiaomei=Person("小美",17,1.65)
xiaomei.eat()

