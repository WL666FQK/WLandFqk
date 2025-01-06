import pandas as pd

# data = {'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [25, 30, 35],
#         'gender': ['F', 'M', 'F']}
#
# df = pd.DataFrame(data)
#
# df.to_excel('data.xlsx', index=False)

df = pd.read_excel('resources/数据.xlsx')
print(df['姓名'])

