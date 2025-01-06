# Author: 王璐
# Date: 2025/1/3
# Time: 8:37

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

dest_addr=('192.168.188.1',2000)

client.connect(dest_addr)
file_name=input("请输入要下载的文件名：")
client.send(file_name.encode('utf8'))

data=client.recv(1024)
if data:
    with open('[接收]'+file_name,'wb') as f:
        f.write(data)

client.close()