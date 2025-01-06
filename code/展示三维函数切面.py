import matplotlib.pyplot as plt
import numpy as np

# 创建x，y数据点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)     # 生成网格坐标矩阵

# 定义三维函数
def f(x,y):
    return x**2 + y**2

# 计算z的值
z = f(x, y)

# 创建图形和轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制表面
surf = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.5)

# 定义要突出显示的点
point_x, point_y = 1.0, 1.0
point_z = f(point_x, point_y)

# 绘制该点
ax.scatter(point_x, point_y, point_z, color='red', s=50)

# 计算切平面的法线
normal = np.array([2*point_x, 2*point_y, -1])

# 定义平面上的点 x_plane,y_plane,z_plane