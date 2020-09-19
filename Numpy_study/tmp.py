import numpy as np
a = np.arange(12).reshape(3,4)
print(np.max(a))
print(np.max(a, axis=0))
print(np.max(a, axis=1))
print('=========')
b1 = np.array([False,True,True])
b2 = np.array([True,False,True,False])
print(a)
print(a[b1,:])

a = "A"
print(ord(a))

b = 100
print(chr(b))
b = 'b'
print(ord(b))
print(chr(96),chr(95))

a = np.array( [20,30,40,50] )
b = np.arange(4)
print(a-b)
print(b**2,10*np.sin(a))
print(a<35)

A=np.arange(0,12).reshape((3,4))
for row in A: print(row)
## 不能直接迭代每一列，但是可以通过对矩阵进行处理，即转矩即可
print('==============')
for column in A.T: print(column)
