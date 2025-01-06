# Author: 王璐
# Date: 2025/1/6
# Time: 17:13

import re

def example1():
    ret=re.match(".","M")
    print(ret.group())

    ret=re.match("t.o","too")
    print(ret.group())

    ret=re.match("t.o","two")
    print(ret.group())

if __name__ == '__main__':
    example1()