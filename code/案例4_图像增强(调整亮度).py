import numpy as np
import cv2

image = cv2.imread('robot.png')    # 读取图像

increased_contrast = cv2.convertScaleAbs(image, alpha=1.5)   # alpha>1,增加对比度

decreased_contrast = cv2.convertScaleAbs(image, alpha=0.5)   # 减少对比度

# 将图片进行横向拼接
combined_image = cv2.hconcat([image, increased_contrast, decreased_contrast])

# 显示图片
cv2.imshow('Original - Increased Contrast - Decreased Contrast', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()