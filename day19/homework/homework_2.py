# Author: 王璐
# Date: 2025/1/4
# Time: 21:14

# 2、创建子进程，能够获取子进程pid并打印
import os
from multiprocessing import Process

def proc():
    print(os.getpid())

if __name__ == '__main__':
    p=Process(target=proc)
    p.start()
    p.join()
