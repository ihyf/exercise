import operator
d = dict()
all_data_list = []
d['hyf1'] = {
        'Project Name': '1',
        'Instances': '2',
        'VCPU': '3',
        'RAM number': '4',
        'SSD': '5',
        'HDD': 6,
        'SATA': '7',
        'Volume Snapshot': '8',
        'Instances Snapshots': '9',
        'Network': '10',
        'Routers': '11',
        'Floating IP': '12',
    }
d['hyf2'] = {
    'Project Name': '7',
    'Instances': '4',
    'VCPU': '8',
    'RAM number': '9',
    'SSD': '1',
    'HDD': 1,
    'SATA': '3',
    'Volume Snapshot': '5',
    'Instances Snapshots': '0',
    'Network': '1',
    'Routers': '55',
    'Floating IP': '10',
}
d['hyf3'] = {
    'Project Name': '14',
    'Instances': '7',
    'VCPU': '9',
    'RAM number': '19',
    'SSD': '12',
    'HDD': 44,
    'SATA': '22',
    'Volume Snapshot': '10',
    'Instances Snapshots': '6',
    'Network': '8',
    'Routers': '11',
    'Floating IP': '16',
}
all_data_list.append(d)


def sort_by_key(data_list, sort_by):
    """sort data by ihyf"""
    # keys list
    key_list = ['Project Name', 'Instances', 'VCPU', 'RAM number', 'SSD', 'HDD', 'SATA',
                'Volume Snapshot', 'Instances Snapshots', 'Network', 'Routers', 'Floating IP']
    sort_by = key_list.index(sort_by)
    # sorted list
    z_list = []
    result_list = []
    for data in data_list:
        for k, v in data.items():
            i_typle = (k, v['Instances'], v['VCPU'], v['RAM number'], v['SSD'], v['HDD'], v['SATA'],
                       v['Volume Snapshot'], v['Instances Snapshots'], v['Network'], v['Routers'], v['Floating IP'])
            z_list.append(i_typle)
    z_list.sort(key=operator.itemgetter(sort_by), reverse=True)
    for z in z_list:
        d = dict()
        d[z[0]] = {key_list[1]: z[1],
                   key_list[2]: z[2],
                   key_list[3]: z[3],
                   key_list[4]: z[4],
                   key_list[5]: z[5],
                   key_list[6]: z[6],
                   key_list[7]: z[7],
                   key_list[8]: z[8],
                   key_list[9]: z[9],
                   key_list[10]: z[10],
                   key_list[11]: z[11]}
        result_list.append(d)
    return result_list

print sort_by_key(all_data_list, "HDD")