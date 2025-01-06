# Author: 王璐
# Date: 2025/1/4
# Time: 20:04

#循环接收
def cycle_recv(client,file,file_size):
    total=0

    while total<file_size:
        data=client.recv(1000)
        file.write(data)
        total+=len(data)