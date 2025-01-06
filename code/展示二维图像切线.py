import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return x ** 2

# 导数（梯度）
def df(x):
    return 2 * x

# 绘制原始函数
x = np.linspace(-3, 3, 100)   # 从-3到3平均拆分成100个点
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^2")

# plt.show()

# 在 x=1 时的梯度和切线
x1 = 1
y1 = f(x1)
slope = df(x1)

# 切线方程：y = m(x-x1) + y1
def tangent_line(x, x1, y1, slope):
    return slope * (x - x1) + y1

# 在切点附近绘制切线
x_tangent = np.linspace(x1 - 1, x1 + 1, 10)
y_tangent = tangent_line(x_tangent, x1, y1, slope)

plt.plot(x_tangent, y_tangent, label="Tangent at x = 1", color='red')  # 切线，绘制折线图
plt.scatter([x1], [y1], color='black')     # 切点

# 设置图像
plt.legend()   # 显示图注信息
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Function and Tangent Line at a Point")
plt.grid(True)   # 背景中有网格
plt.show()
