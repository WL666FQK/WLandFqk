import pandas as pd
#
# data_loc = r'./resources/yolov5s.csv'
# data = pd.read_csv(data_loc)
# print(data)

# data_loc = r'./resources/销售数据.xlsx'
# data = pd.read_excel(data_loc)
# # print(data)
# print(data.describe())

# data_loc = r'./resources/销售数据.xlsx'
# data = pd.read_excel(data_loc)
# print(data.head())
# print(data.tail(7))

# data_0 = data.loc[0]
# print(data_0)

# data_1 = data.loc[:,"大类编码"]
# print(data_1)

# data_2 = data.loc[1, "大类编码"]
# print(data_2)

# data_3 = data.loc[1:3, "大类编码":"中类名称"]
# print(data_3)

# data_4 = data.loc[data["销售数量"]>10]
# print(data_4)
#
# data_5 = data.loc[data["销售数量"] > 10, ["小类编码", "小类名称"]]
# print(data_5)


file_loc = r'./resources/销售数据.xlsx'
data = pd.read_excel(file_loc)

data_extract = data.groupby('商品类型')['销售金额'].sum   # 按照"商品类型"进行分组，并对分组里销售金额求和
data_extract = data_extract.reset_index()

print(data_extract)