# Author: 王璐
# Date: 2024/12/30
# Time: 8:34

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest_addr=('192.168.188.1',2000)
# client.sendto(b'hello',dest_addr)
client.sendto('hello中国'.encode('utf8'),dest_addr) # 放汉字还是不放都行
data,_=client.recvfrom(100)
print(data.decode('utf8'))
client.close()
