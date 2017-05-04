class L(object):
    _l = ['name', 'id']
a = L()
setattr(a, 'name', 'hyf')
print(a.name)
print(a.__dict__)