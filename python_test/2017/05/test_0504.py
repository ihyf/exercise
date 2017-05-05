# coding:utf-8
import operator

# 组装好的原始数据
data_list = [{'hyf1': {'neicun': '4G', 'yunyingpan': '5G', 'cpu': '40%'}},
             {'hyf2': {'neicun': '5G', 'yunyingpan': '6G', 'cpu': '45%'}},
             {'hyf3': {'neicun': '3G', 'yunyingpan': '9G', 'cpu': '35%'}}]


def sort_by_key(sort_by='neicun'):
    # keys list
    key_list = ['username', 'neicun', 'yunyinpan', 'cpu']
    # 根据xx来排序
    sort_by = key_list.index(sort_by)
    print sort_by
    # 排序好的 数据列表
    z_list = []
    for data in data_list:
        for k, v in data.items():
            i_typle = (k, v['neicun'], v['yunyingpan'], v['cpu'])
            z_list.append(i_typle)
    z_list.sort(key=operator.itemgetter(sort_by), reverse=True)
    # 返回的结果列表
    result_list = []
    for z in z_list:
        d = dict()
        d[z[0]] = {key_list[1]: z[1],
                   key_list[2]: z[2],
                   key_list[3]: z[3]}
        result_list.append(d)
    print result_list

sort_by_key('cpu')

