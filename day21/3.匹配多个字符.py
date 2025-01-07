# Author: 王璐
# Date: 2025/1/6
# Time: 22:07

import re

def use_star():
    ret=re.match("[A-Z][a-z]*","M")
    print(ret.group())

    ret=re.match("[A-Z][a-z]*","MnnM")
    print(ret.group())

    ret=re.match("[A-Z][a-z]*","Aadfbj")
    print(ret.group())

def use_plus():
    names=["name1","_name","2_name","__name__"]

    for name in names:
        ret=re.match("[a-zA-Z_]+[\w]*",name)
        if ret:
            print("变量名 %s 符合要求" % ret.group())
        else:
            print("变量名 %s 非法" % name)

# 使用问号
def use_question():
    ret=re.match("[1-9]?[0-9]","7")
    print(ret.group())

    ret = re.match("[1-9]?\d","33")
    print(ret.group())

    ret = re.match("[1-9]?\d","09") # 到开头结尾
    print(ret.group())

def use_m():
    ret=re.match("[a-zA-Z0-9_]{6}","12a3g45678")
    print(ret.group())

    ret=re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
    print(ret.group())


if __name__ == '__main__':
    # use_star()
    # use_plus()
    # use_question()
    use_m()