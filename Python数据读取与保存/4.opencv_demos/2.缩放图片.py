import cv2

image = cv2.imread(r'resources/food.png')    # 读取图片
if image is None:      # 检查图片是否正确加载
    print("Error:Could not load image.")
    exit()

# print(image.shape)   # 获取到一个元组，（高度、宽度、通路），缩放时只需获得宽高
original_height, original_width = image.shape[:2]    # 截取元组的前两个元素，0，1，不包括右边界2
new_width = int(original_width / 2)     # 计算新宽度
new_height = int(original_height / 2)      # 计算新高度

# 使用cv2.resize进行图片缩放，cv2.INTER_AREA为图像插值方法，在图像缩小时具有优异的抗噪声和抗锯齿能力
resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

# 显示原始图片和缩放后的图片
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)     # 让图片停留，等待用户按键，然后关闭窗口
cv2.destroyAllWindows()