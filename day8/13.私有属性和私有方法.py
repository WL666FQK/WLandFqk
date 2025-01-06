class Women:
    def __init__(self,name):
        self.name=name
        # 不要问女生的年龄
        self.__age=18

    def eat(self):
        self.__secret()

    def __secret(self):
        print("我的年龄是 %d" % self.__age)

xiaomei=Women('小美')
print(xiaomei.name)
xiaomei.eat()