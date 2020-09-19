# import numpy as np
### 一、ndarray对象的更重要的属性:
1.ndarray.ndim：数组的轴(维度)个数。在Python世界中，维度的数量被称为rank。
2.ndarray.shape：这是一个整数的元组，表示每个维度中数组的大小。对于有n行和m列的矩阵，shape将是(n,m)。
因此，shape元组的长度就是rank或维度的个数ndim。
3.ndarray.size：数组元素的总数。这等于shape的元素的乘积。
4.ndarray.dtype：一个描述数组元素类型的对象。如：numpy.int32、numpy.int16和numpy.float64等。
5.ndarray.itemsize：数组中每个元素的字节大小;例如，元素为float64类型的数组的itemsize为8（=64/8），而complex32类型的
数组的comitemsize为4（=32/8）。它等于ndarray.dtype.itemsize

### 二、数组的创建方法
## 2.1可以使用array函数从常规Python的列表或元组创建
如：a = np.array([2,3,4])/([[1,2,3],[4,5,6]])/([(1,2,3),[4,5,6]])
# 2.11 创建数组同时可以指定类型
如：a = np.array([[1,2,3],[4,5,6]], dtype=np.int64)
# 2.12 NumPy提供了函数zeros创建一个由0组成的数组;函数ones由1创建的数组;函数empty内容是随机的并取决于存储容器状态
如：a = np.ones((3,2))
## 2.2 NumPy提供了一个类似于range的函数arange，该函数返回数组而不是列表；并且也接受小数
a = np.arange(1,11,2)/a = np.arange(0,2,0.6)
# 2.21 arange配合reshape生成多维数组
a = np.arange(1,21,2).reshape(2,5)
# 2.22 当arange与浮点参数一起使用，由于浮点精度优先，通常不可预测获得元素数量；
# 通常使用函数linspace，它接收我们想要的元素数量而不是步长作为参数
如：a = np.linspace( 0, 2, 9 )     # 9 numbers from 0 to 2
x = np.linspace(0,2*np.pi,10)    # useful to evaluate function at lots of points
f = np.sin(x)

### 三、打印数组
## 3.1 NumPy以与嵌套列表类似的方式显示它，但是具有以下布局：
## 最后一个轴从左到右打印，
## 倒数第二个从上到下打印，
## 其余的也从上到下打印，每个切片与下一个用空行分开。
## 一维数组被打印为行、二维为矩阵和三维为矩阵列表
a = np.arange(6) #1d array
b = np.arange(12).reshape(4,3) # 2d array
c = np.arange(24).reshape(2,3,4)    # 3d array
## 3.2.1 如果数组太大而无法打印，NumPy将自动跳过数组的中心部分并仅打印角点：
print(np.arange(10000).reshape(100,100))
## 3.2.2 要禁用3.2.1此行为并强制NumPy打印整个数组，你可以使用set_printoptions更改打印选项。
np.set_printoptions(threshold=90)
print(np.arange(100).reshape(10,10))
## 3.3 迭代数组
# 3.3.1 简单迭代，仅相当于迭代第一轴
b = np.arange(12).reshape(4,3)
for row in b: print(row)
#3.3.2 迭代出每一个元素，使用flat属性
b = np.arange(12).reshape(4,3)
for row in b.flat: print(row)

### 四、数组运算
## 4.1 数组上的算术运算符使用元素级别。一个新的数组被创建并填充结果。
a = np.array( [20,30,40,50] )
b = np.arange(4)
print(a-b)
print(b**2,10*np.sin(a))
print(a<35)     #返回值[ True  True False False]
## 4.2 与许多矩阵语言不同，乘法运算符*的运算在NumPy数组中是元素级别的。矩阵乘积可以使用dot函数或方法执行：
矩阵运算：矩阵相乘，必须满足矩阵A的列数与矩阵B的函数想等，或者矩阵A的行数与矩阵B的列数相等。
矩阵运算公式：A第一行与B第一列对应相乘的和得C的第一行的第一个值；A第一行与B第二列对应相乘得C的第一行的第二个值；依次计算；
同理：A第二行与B第一列对应相乘的和得C的第二行的第一个值；A第二行与B第二列对应相乘得C的第二行的第二个值；依次计算；
A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0],[3,4]] )
print(A.dot(B)) or print(np.dot(A,B))   # matrix product
## 4.3 比较
# 4.3.1 不加参数默认取一个
最大值：np.max(A) ；最小值：np.min(A)；平均值：np.mean(A)
# 4.3.2 加axis参数，则按行列取(axis为维度，所以值不超过数组的维度ndim)
np.max(A,axis=0)    np.max(A,axis=1)

### 五、数组的切片
# A=np.arange(0,12).reshape((3,4)) 索引也是0开始
[[ 0  1  2  3] [ 4  5  6  7] [ 8  9 10 11]]
## 5.1 逗号前表示按行方向，逗号后表示列方向
# 如：A[1]:取数组第二行； # [4 5 6 7]
A[1,1:3]:取数组第二行的第二列到第三列; # [5 6]
A[1:3,1]:取数组第二行、第三行的第二列; # [5 9]
## 5.2 迭代每一行
for row in A: print(row)
## 不能直接迭代每一列，但是可以通过对矩阵进行处理，即转矩即可
for column in A.T: print(column)

### 六、数组合并
## 6.1 直接合并
A=np.array([1,1,1])
B=np.array([2,2,2])
C=np.vstack((A,B)) # vertical stack 垂直方向合并 [[1 1 1] [2 2 2]] 
D=np.hstack((A,B)) # horizontal stack   水平方向合并 [1 1 1 2 2 2]
## 6.2 添加维度
A=np.array([1,1,1])
C=A[:,np.newaxis]   # A变成纵向的 [[1] [1] [1]]
## 6.3 concatenate多个函数的合并，还可以设置在哪个维度合并
A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
C=np.concatenate((A,B,B,A),axis=0) # axis=0纵向合并，axis=1横向合并

### 七、 数组分割
## 7.1 np.split 相等分割，不支持不等分割
A=np.arange(12).reshape(3,4)
C=np.split(A,2,axis=1) # axis=0行分割，axis=1列分割
## 7.2 np.array_split支持不等分割
A=np.arange(12).reshape(3,4)
C=np.split(A,3,axis=1) # axis=0行分割，axis=1列分割
## np.vsplit(A,3)   # 行分割
## np.hsplit(A,2)   # 列分割

