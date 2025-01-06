# Author: 王璐
# Date: 2024/12/30
# Time: 10:19

import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('192.168.188.1',2001)
server.bind(addr)
data,client_addr=server.recvfrom(100)
print(data.decode('utf8'))
print(client_addr)
server.sendto("这是一个作业，我是服务器端发来的".encode('utf8'),client_addr)
server.close()