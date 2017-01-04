# coding:utf-8
import string
import random
'''
    # 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券）
    # 使用 Python 如何生成 200 个激活码（或者优惠券）
'''

LENGTH=20
GESHU=2
def base_str():  # 字母数字字符串
    return string.letters + string.digits
def get_one_jihuoma():
    list=[random.choice(base_str()) for i in range(LENGTH)]
    one_jihuoma=(''.join(list))
    return one_jihuoma
def get_all_jihuoma():
    for i in range(GESHU):
        print get_one_jihuoma()

if __name__=='__main__':
    get_all_jihuoma()


