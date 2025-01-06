# Author: 王璐
# Date: 2025/1/4
# Time: 22:36

# 4、创建两个子进程，一个子进程写消息队列，一个读消息队列（依次写入 A，B，C），确保写的内容，读的进程，读取完毕并打印
import time
from multiprocessing import Process,Queue


def writer(q:Queue):
    list=['A','B','C']
    for i in list:
        print("Puts %s in queue..." % i)
        q.put(i)
        time.sleep(1)


def reader(q:Queue):
    while True:
        if not q.empty():
            value=q.get(True)
            print('Get %s from queue.........' % value)
            time.sleep(2)
        else:
            break



if __name__ == '__main__':
    q=Queue(10)
    p_writer=Process(target=writer,args=(q,))
    p_reader=Process(target=reader,args=(q,))
    p_writer.start()
    time.sleep(1)
    p_reader.start()
    p_writer.join()
    p_reader.join()


