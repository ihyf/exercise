# coding:utf-8


def get_list(str_s, str_t):
    a = []
    b = [i for i in range(len(str_s))]
    for t in str_t:
        a.append(str_s.find(t))
    b = set(b)
    a = set(a)
    c = list(b-a)
    d = []
    length = len(str_s)-len(str_t)
    for i in range(length):
        d.append(c[i])
    return d
if __name__ == "__main__":
    str_s = 'rabbbit'
    str_t = 'rabbit'
    result2 = get_list(str_s, str_t)
    print result2
