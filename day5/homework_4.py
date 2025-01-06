def contain_one_num(a):
    result = 0
    while a:
        result += a & 1
        a=a>>1

    print("该整数的二进制包含1的个数为：%d" % result)



if __name__ == '__main__':
    i = int(input("请输入一个数："))
    contain_one_num(i)