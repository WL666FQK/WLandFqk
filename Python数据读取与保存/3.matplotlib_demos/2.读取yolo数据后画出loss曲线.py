import pandas as pd
import matplotlib.pyplot as plt

data_loc = r'./resources/yolov5s.csv'

data = pd.read_csv(data_loc, index_col=0)    # index_col=0表示第一列为index值

train_bbox_loss = data['      train/box_loss']   # 提取这一列数据的值

x_list = [i for i in range(len(train_bbox_loss))]   # 从0开始到长度个
plt.plot(x_list, train_bbox_loss)    # plt.plot(x,y）
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('YOLOv5s')
plt.show()