# Author: 王璐
# Date: 2025/1/4
# Time: 18:42

from multiprocessing import Process,Queue
import time

def writer(q:Queue):
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(1)

def reader(q:Queue):
    while True:
        if not q.empty():
            value=q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(2)
        else:
            break

if __name__ == '__main__':
    q=Queue(10)
    pw=Process(target=writer,args=(q,))  # 一个元素必须加逗号，才是元组
    pr=Process(target=reader,args=(q,))
    pw.start()
    time.sleep(1)
    pr.start()
    pw.join()
    pr.join()