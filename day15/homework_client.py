# Author: 王璐
# Date: 2024/12/30
# Time: 10:19

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest_addr=('192.168.188.1',2001)
client.sendto('这是作业，我是客户端发来的'.encode('utf8'),dest_addr)
data,server_addr=client.recvfrom(100)
print(data.decode('utf8'))
print(server_addr)
client.close()
