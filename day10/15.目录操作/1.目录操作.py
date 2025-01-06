# Author: 王璐
# Date: 2024/10/18


import  os

def use_name():
    os.rename('file1','file')

def use_remove():
    os.remove('file')

def use_listdir():
    print(os.listdir('.'))

def dir_dfs(path,width):
    file_list=os.listdir(path)
    for filename in file_list:
        print(' '*width+filename)
        if os.path.isdir(path+'/'+filename):  # 如果是目录
            dir_dfs(path+'/'+filename,width+4)

if __name__ == '__main__':
    # use_name()
    # use_remove()
    # use_listdir()
    dir_dfs('.',0)