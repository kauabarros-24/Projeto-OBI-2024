m = dict()

m = {'a': 1, 'b': 2, 'c': 3}

m['d'] = 4

del m['a']

print(next(iter(m)))

print('a' in m)

for c, k in m.items():
    print(c, k)

