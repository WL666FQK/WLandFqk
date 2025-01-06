# Author: 王璐
# Date: 2025/1/4
# Time: 23:01

# 5、创建进程池，进程池中一个进程往queue中写，一个读并打印
import os
import time
from multiprocessing import Manager,Pool

def writer(q):
    print("writer进程启动(%s),父进程为(%s)" % (os.getpid(),os.getppid()))
    for i in "冯奇康":
        q.put(i)

def reader(q):
    print("reader进程启动(%s),父进程为(%s)" % (os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到的信息：%s" % q.get())


if __name__ == '__main__':
    q=Manager().Queue()
    po=Pool()  # 初始化进程池
    po.apply_async(writer,args=(q,))
    time.sleep(1)
    po.apply_async(reader,args=(q,))
    po.close()
    po.join()

