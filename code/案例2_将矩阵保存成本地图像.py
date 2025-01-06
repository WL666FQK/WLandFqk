import numpy as np
import cv2     # 导入OpenCV模块

# 创建一个大小为224x224的二维矩阵，值为0~255之间
two_d_matrix = np.random.randint(0, 256, (224, 224), dtype=np.uint8)

# 创建一个大小为 3x224x224 的三维矩阵，值为0~255之间，第一个值代表通道数
three_d_matrix = np.random.randint(0, 256, (3, 244, 244), dtype=np.uint8)


# 在OpenCV中，图像的通道顺序为 高 x 宽 x 通道数
three_d_matrix_transposed = three_d_matrix.transpose(1, 2, 0)

# 将画面显示出来
cv2.imshow('two_d_matrix', two_d_matrix)
cv2.imshow('three_d_matrix', three_d_matrix_transposed)
cv2.waitKey(0)

# 使用OpenCV将图片保存到本地
cv2.imwrite("two_d_matrix.jpg", two_d_matrix)
cv2.imwrite("three_d_matrix.jpg", three_d_matrix_transposed)