import cv2

cap = cv2.VideoCapture(0)

# 检查是否成功打开摄像头
if not cap.isOpened():
    print("Error:Could not open camera.")
    exit()

# 获取摄像头的帧宽度和帧高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定义视频编码器和输出文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 或者使用XVID，将视频保存成MP4文件
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))  # 20为帧率，20fps，即每秒传输20个帧

while True:
    ret, frame = cap.read()  # 读取画面
    if not ret:
        print("Failed to grab frame.")
        break

    out.write(frame)    # 将当前帧写入VideoWriter中进行画面写入
    cv2.imshow('frame', frame)    # 显示当前帧

    if cv2.waitKey(1) & 0xFF == ord('q'):    # 按'q'键退出循环
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()