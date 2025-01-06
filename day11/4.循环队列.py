# Author: 王璐
# Date: 2024/10/19

from collections import deque

#增删改查
queue = deque(["Eric","John","Michael"])
queue.append('luke')
print(queue)
print(queue.popleft())
print(queue)

queue[0] = 'xiongda'
print(queue[0])
print(queue)
