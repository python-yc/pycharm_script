# -*- coding: utf-8 -*-
import numpy as np

# 使用numpy库函数生成的数组，使用时不能联想对应的属性；
# 而自定义列表然后再生成数组就可以联想，不知道为什么
array = np.arange(15).reshape(3,5)
print(array)
print(array.ndim)

b = [[ 0,  1,  2,  3,  4],
     [ 5,  6,  7,  8,  9],
     [10, 11, 12, 13, 14]]
array = np.array(b)
print(array)
print("ndarray的属性ndim,shape,size,dtype,itemsize,data值分别为：")
print(array.ndim, array.shape, array.size, array.dtype, array.itemsize,array.data, sep="\t")

a = np.array([(1,2,3),[4,5,6]], dtype=np.int64)
print(a)
print(np.ones((3, 4)))
#=================================
#数组上的算术运算符使用元素级别。一个新的数组被创建并填充结果。
a = np.array( [20,30,40,50] )
b = np.arange(4)
print(a-b)
print(b**2,10*np.sin(a))
print(a<35)     #返回值[ True  True False False]

