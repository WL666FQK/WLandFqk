# Author: 王璐
# Date: 2025/1/4
# Time: 20:08

from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到的消息：%s" % q.get(True))


def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(),os.getppid()))
    for i in "fengqikang":
        q.put(i)

if __name__ == '__main__':
    q=Manager().Queue()
    po=Pool() # 初始化进程池
    po.apply_async(writer,args=(q,))
    time.sleep(1)
    po.apply_async(reader,args=(q,))
    po.close()
    po.join()

