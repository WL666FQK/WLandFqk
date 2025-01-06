# Author: 王璐
# Date: 2024/12/25

# 使用python的队列deque

from collections import deque

queue=deque(["Eric","John","Michael"])
queue.append('luke')
print(queue)
print(queue.popleft())

queue[0]='xiongda'
print(queue)