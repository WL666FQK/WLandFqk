# Author: 王璐
# Date: 2024/10/18


# 2、通过 try 进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是
# 对称数，12321 就是对称数，123321 也是对称数，否则就不是，非整型抛异常，非对
# 称数抛不抛异常自行选择

try:
    num=int(input('请输入一个整数：'))
    string1=str(num)
    string2=string1[::-1]  # 将字符串反转
    # print(string2)
    if string1==string2:
        print("%d是对称数" % num)
    else:
        print("%d不是对称数" % num)
    # print(string1)
    # print(type(string1))

except:
    print("请输入整数！！！")