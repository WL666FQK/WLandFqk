# 6、设计一个类，实例化 1 个对象，会实现下面两种行为
# 需求
# • 一只 黄颜色 的 狗狗 叫 大黄
# • 具有 汪汪叫 行为
# • 具有 摇尾巴 行为
class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        print("%s 的 %s 在汪汪叫" % (self.color,self.name))

    def shake(self):
        print("%s 的 %s 在摇尾巴" % (self.color,self.name))

dahuang=Dog("大黄","黄色")
dahuang.bark()
dahuang.shake()
