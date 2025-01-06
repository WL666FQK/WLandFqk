import numpy as np

# 定义矩阵A和B
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 定义标量C
C = 3

# 标量与矩阵的乘法
scalar_matrix_multiplication = C * A

# 矩阵的加法
matrix_addition = A + B

print(scalar_matrix_multiplication, '\n', matrix_addition)