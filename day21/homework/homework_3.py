# Author: 王璐
# Date: 2025/1/7
# Time: 9:37

# 3.练习上课的0-99的数字匹配

import re

number=input("请输入数字：")

ret=re.match("^[1-9]?[0-9]$",number)
if ret:
    print(ret.group())
else:
    print("不属于0-99")