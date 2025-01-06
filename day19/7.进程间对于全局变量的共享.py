# Author: 王璐
# Date: 2025/1/4
# Time: 16:09

import os
import time
from multiprocessing import Process

nums=[11,22]
def work1():
    print('I am work1,{}'.format(os.getpid()))
    nums.append(33)
    print(nums)

def work2():
    print('I am work2,{}'.format(os.getpid()))
    print(nums)

if __name__ == '__main__':
    p=Process(target=work1)
    p.start()
    p.join()
    p=Process(target=work2)
    p.start()
    p.join()
