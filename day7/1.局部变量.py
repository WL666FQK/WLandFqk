def demo1():
    num = 10
    print(num)
    num = 20
    print("修改后 %d" % num)


def demo2():
    num=100
    print(num)


# 局部变量修改相互之间不影响
demo1()
demo2()
print("over")