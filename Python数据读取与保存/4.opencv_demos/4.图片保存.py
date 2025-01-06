import cv2

image = cv2.imread('resources/food.png')   # 读取图像

if image is not None:    # 如果图像不为空，则保存图像
    cv2.imwrite('output_image.png', image)  # 第一个参数是保存成什么样的名称，第二个参数是要保存的图片
else:
    print("无法读取图像")
