# Author: 王璐
# Date: 2025/1/3
# Time: 17:58

import struct
import os
import time

train_content='我很帅你很牛'.encode('utf8')
train_head=len(train_content)
print(train_head)
print(type(train_head))
print('-'*50)
train_head_bytes=struct.pack('I',train_head)
print(train_head_bytes)

b=struct.unpack('I',train_head_bytes)
print(b[0])