# coding:utf-8


def get_result(list_a):
    b = []
    list_a.sort()
    mark = 1
    for i in range(len(list_a)-1):
        if list_a[i]+1 == list_a[i+1]:
            mark+=1
        else:
            mark = 1
        b.append(mark)
    return max(b)

if __name__ == "__main__":
    list_a = [100, 4, 200, 3, 2, 1, 101, 5, 6]
    result = get_result(list_a)
    print result
