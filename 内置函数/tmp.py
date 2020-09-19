# -*- coding: utf-8 -*-
import numpy as np

data = [[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]]
arry = np.array(data,dtype=np.int64)
print(arry)

print('====')
print(arry.data,arry.ndim,arry.dtype,arry.shape,arry.size,arry.itemsize)
