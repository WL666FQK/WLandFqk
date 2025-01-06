# Author: 王璐
# Date: 2024/10/18

import os

# 3、以可读可写打开一个文件，然后写入“人生苦短 我用 Python”，关闭文件
def use_write():
    file = open('file1.txt', mode='w+', encoding='utf8')
    file.write('今天是2024年10月18日，祝冯奇康生日快乐')
    file.close()


# 6、通过 seek 从文件开头偏移 5 个字节，然后把文件剩余内容读取
def use_seek():
    file = open('file3.txt', mode='r+', encoding='utf8')
    file.write('fqk祝你生日快乐')
    # print(text)
    file.seek(9)
    text = file.read()
    print(text)
    file.close()

# 9、对文件进行改名并删除文件
def use_rename():
    os.rename('file4','file_rename')
    os.remove('file_rename')

# 10、创建文件夹，删除文件夹（均使用相对路径），改变程序执行路径，获取程序当前路径
def use_dir():
    os.mkdir('dir1')
    os.mkdir('dir2')
    os.mkdir('dir2/dir3')
    os.rmdir('dir1')
    print(os.getcwd())


if __name__ == '__main__':
    # use_write()
    use_seek()
    # use_rename()
    # use_dir()