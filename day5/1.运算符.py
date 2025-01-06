# 定义一个函数，通过def，下面是算术运算
def calc():
    print(5 / 2)  # 非整除
    print(5 // 2)  # 整除
    print(5 % 2)  # 取余 取模
    print(2 ** 3)  # 2的3次方
    print(3 + 5 - 2)  # 同级运算符从左至右运算


# 关系运算
def relation():
    num = int(input("请输入一个数："))
    print(3 < num < 10)  # python支持某个数关系运算符连写


# 逻辑运算
def logic():
    # year=int(input("请输入年份："))  # 判断是否是闰年的条件，能被4整除但不能被100整除，能被400整除
    # print(year%400==0 or year%4==0 and year%100!=0)
    print(5 and 3)
    print(5 or 3)


# 赋值运算符
def assign():
    a = 3
    a += 4
    print(a)
    b = 100
    a, b = b, a
    print(a, b)


# 位运算
# 只能对整数
def bit():
    i = 5
    j = 7
    print(i & j)  # 5
    print(i | j)  # 7
    print(i ^ j)  # 异或 2
    print(~i)  # 按位取反
    print(i << 1)  # 左移乘2
    print(i >> 1)  # 右移是整除2


if __name__ == '__main__':
    # calc()
    # relation()
    # logic()
    assign()
    # bit()
