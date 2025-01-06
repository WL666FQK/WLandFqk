import numpy as np

# 定义矩阵A
A = np.array([[4, 1],
              [2, 3]])

# 使用Numpy求特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

print("特征值：", eigenvalues)
print("特征向量：", eigenvectors)