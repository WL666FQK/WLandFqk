import cv2

# 创建一个VideoCapture对象，参数0表示使用默认的摄像头，也可以传入一个视频文件的路径
cap = cv2.VideoCapture("resources/piano.mp4")

while True:
    ret, frame = cap.read()   # 读取一帧
    if ret:
        cv2.imshow('Frame', frame)   # 如果读取成功，显示这一帧

    if cv2.waitKey(1) & 0xFF == ord('q'):   # 按'q'键退出循环
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()