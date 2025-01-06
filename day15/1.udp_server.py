# Author: 王璐
# Date: 2024/12/30
# Time: 8:22

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('192.168.188.1',2000)  # 写1024以上的端口
s.bind(addr)  # 失败直接抛异常
data,client_addr=s.recvfrom(100) # 100代表接的长度
print(data.decode('utf8'))
print(client_addr)
s.sendto('很牛'.encode('utf8'),client_addr)
s.close()