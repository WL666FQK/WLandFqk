import cv2
import numpy as np

def add_gaussian_noise(image):
    row, col = image.shape  # image.shape 返回一个表示图像形状的元组，具体的含义是 (height, width, channels)
    mean = 0    # 平均值
    sigma = 15   # 标准差
    gauss = np.random.normal(mean, sigma, (row, col))  # 返回一组符合高斯分布的概率密度随机数
    noisy = image + gauss
    noisy_img = np.clip(noisy, 0, 255)   # 截取函数，取值范围在0-255之间
    return noisy_img.astype(np.uint8)

# 输入和输出视频文件名
input_video = 'resources/outdoor.mp4'
output_video = 'resources/output.mp4'

cap = cv2.VideoCapture(input_video)   # VideoCapture是一个用于捕捉视频的类，它可以访问计算机的摄像头，或从视频文件中读取图像

# 获取视频的帧率和帧大小
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int((cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 计算新的帧大小(540p)
new_height = 540
new_width = int((new_height / frame_height) * frame_width)

# 创建视频写入对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, new_height), isColor=False)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 调整帧大小
    frame = cv2.resize(frame, (new_width, new_height))

    # 转换为灰度图像
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 水平翻转画面，filename表示需要操作的图像，flipcode表示翻转方式，若为1则表示水平翻转，若为0则表示垂直翻转，若为-1则表示水平垂直翻转
    frame = cv2.flip(frame, 1)

    # 添加高斯噪声
    frame = add_gaussian_noise(frame)

    # 写入输出视频
    out.write(frame)

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()

