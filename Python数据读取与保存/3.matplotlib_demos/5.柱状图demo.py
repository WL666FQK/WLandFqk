import matplotlib.pyplot as plt
import numpy as np

labels = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

x = np.arange(len(labels))   # 设置标签的位置，设置标签长度个x
plt.bar(x, values, color='blue', align='center', alpha=0.7)    # 绘制柱状图

# 设置图标的标题和轴标签
plt.title('Simple Bar Chart')
plt.xlabel('Labels')
plt.ylabel('Values')

plt.xticks(x, labels)   # 设置x轴的标签，让其是labels里的元素
plt.show()   # 显示图像
