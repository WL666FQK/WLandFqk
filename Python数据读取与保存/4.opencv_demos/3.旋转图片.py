import cv2

image = cv2.imread('resources/food.png')

rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)     # 顺时针旋转90°
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)        # 顺时针旋转180°
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)    # 顺时针旋转270°

cv2.imshow('original', image)
cv2.imshow('90 degree', rotated_90)
cv2.imshow('180 degree', rotated_180)
cv2.imshow('270 degree', rotated_270)

cv2.waitKey(0)     # 让图片停留，等待用户按键，然后关闭窗口