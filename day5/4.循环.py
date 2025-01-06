def use_while():
    # 1.定义重复次数计数器
    i = 1

    # 2.使用while判断条件
    while i <= 5:
        # 要重复执行的代码
        # print("Hello Python")
        pass
        # 处理计数器i
        # i = i + 1

    print("循环结束后的 i = %d" % i)


def cal_sum():
    # 计算 0 ~ 100 之间所有数字的累计求和结果
    # 0. 定义最终结果的变量
    result = 0

    # 1.定义一个整数的变量记录循环的次数
    i = 0

    # 2.开始循环
    while i <= 100:
        result += i
        i += 1
    # print("")
    print("0~100之间的数字求和结果 = %d" % result)


if __name__ == '__main__':
    # use_while()
    cal_sum()
