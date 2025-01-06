# Author: 王璐
# Date: 2025/1/4
# Time: 16:41

from multiprocessing import Queue
q=Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
q.put(1)
q.put(2)
print(q.full())  # False
q.put(3)
print(q.full()) # True
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# q.put(4)  # 队列满了后，再放会阻塞
try:
    q.put("消息4",False)
except:
    print("消息队列已满，现有消息数量：%s"%q.qsize())