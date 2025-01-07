# Author: 王璐
# Date: 2025/1/7
# Time: 9:18

# 2.练习上课的163邮箱匹配

import re

email=input("请输入你的163邮箱：")
ret=re.match("[a-zA-Z0-9_]+@163\.com",email)
if ret:
    print("你的163邮箱为：%s" % ret.group())
else:
    print("不符合")