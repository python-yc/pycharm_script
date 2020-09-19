# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
l = ['one', 'two', 'three']

a = set((1,))
print(a)
n = [1, 2, 3]

d = dict(zip(l, n))
print(d)
print(sorted(d.items(), key=lambda x:x[0]))

d2 = dict(sorted(d.items(), key=lambda x:x[0], reverse=True))
print(d2)
