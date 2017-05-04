# coding:utf-8
import operator


data_list = [{'hyf1': {'neicun': '4G', 'yunyingpan': '5G', 'cpu': '40%'}},
             {'hyf2': {'neicun': '5G', 'yunyingpan': '6G', 'cpu': '45%'}},
             {'hyf3': {'neicun': '3G', 'yunyingpan': '9G', 'cpu': '35%'}}]


def sort_by_key(sort_by='neicun'):
    key_list = ['username', 'neicun', 'yunyinpan', 'cpu']
    sort_by = key_list.index(sort_by)
    print sort_by
    z_list = []
    for data in data_list:
        for k, v in data.items():
            i_typle = (k, v['neicun'], v['yunyingpan'], v['cpu'])
            z_list.append(i_typle)
    z_list.sort(key=operator.itemgetter(sort_by), reverse=True)
    result_list = []
    for z in z_list:
        d = dict()
        d[z[0]] = {key_list[1]: z[1],
                   key_list[2]: z[2],
                   key_list[3]: z[3]}
        result_list.append(d)
    print result_list

sort_by_key('cpu')

