# coding:utf-8

from math import sqrt


critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.0,
        'The Night Listener': 3.5
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
        'The Night Listener': 3.0
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'Just My Luck': 1.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 1.0,
        'The Night Listener': 3.0
    },
}


# 欧几里德距离评价


def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if not si:
        return 0

    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1/1+sqrt(sum_of_squares)

# 皮尔逊相关系数
'''在它数据不是很规范（如影评者对影片的评价总是相对平均水平偏离很大时）会倾向更好的结果'''


def sim_pearson(prefs, p1, p2):
    # 得到双方都评价过的列表
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    if not si:
        return 1

    # 项数
    n = len(si)

    # 所有偏好求和
    sum1 = sum([prefs[p1][x] for x in si])
    sum2 = sum([prefs[p2][x] for x in si])

    # 求平方和
    sum1_sq = sum([pow(prefs[p1][x], 2) for x in si])
    sum2_sq = sum([pow(prefs[p2][x], 2) for x in si])

    # 求乘机之和
    p_sum = sum([prefs[p1][x] * prefs[p2][x] for x in si])

    # 计算皮尔逊相关系数
    num = p_sum-(sum1*sum2/n)
    den = sqrt((sum1_sq-pow(sum1, 2)/n)*(sum2_sq-pow(sum2, 2)/n))
    if den == 0:
        return 0
    r = num/den
    return r


# 为评论者打分
def top_matches(prefs, person, n=5, simillarity=sim_pearson):
    scores = [(sim_pearson(prefs, person, other), other)
              for other in prefs if other != person]

    # 对列表进行排序，评价值最高者排在最前面
    scores.sort()
    scores.reverse()
    return scores[0:n]



