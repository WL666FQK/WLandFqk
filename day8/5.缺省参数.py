# 缺省参数指传参时可以不传对应参数
def print_info(name,gender=True):
    gender_text="男生"
    if not gender: # not gender为true 执行下面的句子
        gender_text = "女生"

    print("%s 是 %s" % (name,gender_text))

if __name__ == '__main__':
    print_info('xiongda',False)