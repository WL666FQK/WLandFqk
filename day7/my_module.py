



def print_line():
    print('*'*50)


if __name__ == '__main__':  # 为了实现一切皆模块
    name = 'xiaoxiaoguai'  # 虽然是全局变量，但是对外部可见
    print(__name__)