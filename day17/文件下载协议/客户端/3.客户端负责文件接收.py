# Author: 王璐
# Date: 2025/1/3
# Time: 19:20

from socket import *
import struct
tcp_client_socket=socket(AF_INET,SOCK_STREAM)

# 本地IP地址和端口
address=('192.168.188.1',2000)

# 连接服务器
tcp_client_socket.connect(address)

# 每次要先读4个字节的火车头
train_head_bytes=tcp_client_socket.recv(4)
train_content_len=struct.unpack('I',train_head_bytes)
file_name=tcp_client_socket.recv(train_content_len[0]) # 接到文件名
f=open(file_name.decode('utf8'),'wb')

# 接文件内容的长度
train_head_bytes=tcp_client_socket.recv(4)
train_content_len=struct.unpack('I',train_head_bytes)
file_content=tcp_client_socket.recv(train_content_len[0]) # 接文件内容
f.write(file_content)

f.close()
tcp_client_socket.close()
