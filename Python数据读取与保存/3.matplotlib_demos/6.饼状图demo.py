import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]   # 各扇形所占比例大小
labels = ['A', 'B', 'C', 'D']    # 每一个部分的标签的名字
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']   # 各个部分的颜色
explode = (0.1, 0, 0, 0)   # 突出显示第一个部分

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')    # x,y轴刻度等长，这样扇形图就是一个圆
plt.show()   # 显示图像