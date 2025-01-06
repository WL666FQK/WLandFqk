#10、练习继承、使用 super 调用父类方法，多重继承
class Animal:
    def __init__(self,name):
        self.name=name

    def run(self):
        print('%s会跑' % self.name)

    def eat(self):
        print('%s会吃' % self.name)

class Color:
    def __init__(self, name):
        self.name = name

    def color(self):
        print('%s是黄色的' % self.name)

class Dog(Animal,Color):
    def shake(self):
        print('%s会摇尾巴' % self.name)

    def run(self):
        super().run()
        print('%s会跑得很快' % self.name)

dahuang=Dog('大黄')
dahuang.run()
dahuang.eat()
dahuang.shake()
dahuang.color()