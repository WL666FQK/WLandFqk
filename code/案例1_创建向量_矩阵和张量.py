import numpy as np

# 创建向量(一维)
vector = np.array([1, 2, 3, 4, 5])     # 向量
vector_norm = np.linalg.norm(vector)    # 向量的范数，范数是一种将向量映射到非负实数的函数
print("Vector:\n", vector)
print("Vector L2 Norm:", vector_norm)


# 创建矩阵(二维)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix_norm = np.linalg.norm(matrix)
print("Matrix:\n", matrix)
print("Matrix L2 Norm:", matrix_norm)

# 创建张量(三维)
tensor = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
tensor_norm = np.linalg.norm(tensor)
print("Tensor:\n", tensor)
print("Tensor L2 Norm:", tensor_norm)