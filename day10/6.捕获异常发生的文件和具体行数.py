# Author: 王璐
# Date: 2024/10/16

try:
    print(a)
except Exception as e:
    print(e)
    print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
    print(e.__traceback__.tb_lineno) # 打印异常发生