# Author: 王璐
# Date: 2024/12/27
# Time: 19:56
import random

# 实现一千个随机数(0-10000)之间的去重
class BitMap:
    def __init__(self):
        self.bitmap=0
        self.arr=[]
        for i in range(0,1000):
            self.arr.append(random.randint(1,10000))
        self.newarr=[]

    def duplicate_remove(self):
        for i in self.arr:
            if self.bitmap & 1<<i:
                pass
            else:
                self.newarr.append(i)
                self.bitmap =self.bitmap|1<<i

if __name__ == '__main__':
    b=BitMap()
    b.duplicate_remove()
    print(b.newarr)