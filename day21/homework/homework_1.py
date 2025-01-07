# Author: 王璐
# Date: 2025/1/7
# Time: 9:03

# 1.写一个正则表达式，使其能同时识别下面所有的字符串：'bat','bit', 'but', 'hat', 'hit', 'hut'

import re

list=['bat','bit', 'but', 'hat', 'hit', 'hut']
for i in list:
    # print(i)
    ret = re.match("[bh][aiu][t]$",i)
    if ret:
        print(ret.group())
    else:
        pass