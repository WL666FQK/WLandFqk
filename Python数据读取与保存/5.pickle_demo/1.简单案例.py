import pickle

# 示例数据
data = {
    'name': 'John',
    'age': 30,
    'is_student': False,
    'grades': [85, 90, 78, 92]
}

# 使用pickle保存数据
with open('data.pkl', 'wb') as file:   # wb表示二进制写入
    pickle.dump(data, file)

# 使用pickle加载数据
with open('data.pkl', 'rb') as file:    # rb表示读取二进制文件
    loaded_data = pickle.load(file)

print(loaded_data)