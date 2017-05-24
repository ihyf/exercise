# coding:utf-8
# r_list = []
# d1 = {"hyf1": "1"}
# d2 = {"hyf1": "1"}
# r_list.append(d1)
# r_list.append(d2)
# import json
# z = r_list[:1]
# x = json.dumps([])
# print x
import operator

z = [(1,44),(8,6),(2,1)]
z.sort(key=operator.itemgetter(0),reverse=True)
print z