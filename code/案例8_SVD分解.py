import cv2
import numpy as np

# 读取图像
image = cv2.imread('robot.bmp', 0)    # 读取为灰度图像

# 对图像进行svd分解。np.float64双精度浮点数类型，image.astype可以对数据类型进行转换
U, S, V = np.linalg.svd(image.astype(np.float64), full_matrices=False)

# 定义要保留的奇异值数量
k = 10   # 用前十个最大的特征值重构
s_k = np.diag(S[:k])

# 重构图像
compressed_image = np.dot(U[:, :k], np.dot(s_k, V[:k, :]))
compressed_image = np.clip(compressed_image, 0, 255).astype(np.uint8)  # uint8无符号整数类型

# 显示图像
cv2.imshow('Original Image', image)
cv2.imshow('Compress Image', compressed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()