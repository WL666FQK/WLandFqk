# Author: 王璐
# Date: 2025/1/6
# Time: 23:52

import re

def use_email():
    email_list=["xiaoWang@163.com","xiaoWang@163.comheihei",".com.xiaowang@qq.com"]

    for email in email_list:
        ret=re.match("[\w]{4,20}@163\.com$",email) # 加$符号表示字符串必须以什么结尾
        if ret:
            print("%s 是符合规定的邮件地址，匹配后的结果是：%s" % (email,ret.group()))
        else:
            print("%s 不符合要求" % email)

# 只要0-99
def use_099():
    ret = re.match("^[1-9]?\d$","09") # 到开头结尾
    print(ret.group())

if __name__ == '__main__':
    # use_email()
    use_099()