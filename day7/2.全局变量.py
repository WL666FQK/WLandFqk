# 定义一个全局变量
num = 10


def demo1():
    # num = 20  # 并没有修改到全局变量，只是定义了一个局部变量
    global num   # 加上global之后就是全局变量了
    num = num+20
    print(num)


def demo2():
    print(num)


# 针对全局变量，读的时候可以不加global，要修改的时候，要加上
demo1()
demo2()

print("over")