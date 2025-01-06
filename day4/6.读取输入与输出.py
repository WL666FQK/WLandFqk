x=input('请输入：') # 无论输入123还是abc，x得到的都是字符串
print(float(x)/2)

name='xiaowang'
student_no=1001
price=98.2
weight=6.52
money=price*weight
scale=0.91
print("我的名字叫 %s，请多多关照！" % name)
print("我的学号是 %06d" % student_no)
print("苹果单价 %.2f 元/斤，购买 %.02f 斤，需要支付 %9.03f 元" % (price,weight,money))
print("数据比例是 %.02f%%" % (scale * 100))