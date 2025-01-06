import cv2   # opencv库的名称

img_path = r'resources/food.png'

image_color = cv2.imread(img_path, cv2.IMREAD_COLOR)  # 以彩色模式读取图片，若没有第二个参数，默认为彩色
image_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)   # 以灰度模式读取图片

cv2.imshow('Color Image', image_color)       # 显示图片，引号里为窗口名称
cv2.imshow('Grayscale Image', image_gray)

cv2.waitKey(0)     # 让图片停留，等待用户按键，然后关闭窗口
cv2.destroyAllWindows()