# Author: 王璐
# Date: 2024/10/16

try:
    num=int(input('请输入一个整数：'))
    result=8/num
    print(result)
except ValueError:
    print('请输入正确的整数')
except ZeroDivisionError:
    print('除0错误')
except Exception as result:   # 所有没有提前设置的异常都会走到这里
    print("未知错误 %s" % result)
else:
    print("正常执行")
finally:
    print("无论是否有异常都会执行")

