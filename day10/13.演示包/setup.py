# Author: 王璐
# Date: 2024/10/17

from distutils.core import setup

setup(name="wd_message",  # 包名，不能写错
      version='1.0',
      description="wangdao's发送和接收消息模块", # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="wanglu", # 作者
      author_email="1797575767@qq.com",  # 作者邮箱
      url="www.cskaoyan.com",  # 主页
      py_modules=["wd_message.send_message",  # 也不要写错
                  "wd_message.recv_message"])