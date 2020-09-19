# import pandas as pd, numpy as np
# https://www.cnblogs.com/nxld/p/6058591.html
## 一、数据结构
在pandas中有两类非常重要的数据结构，即序列Series和数据框DataFrame。
Series类似于numpy中的一维数组，除了通吃一维数组可用的函数或方法，
而且其可通过索引标签的方式获取数据，还具有索引的自动对齐功能；
DataFrame类似于numpy中的二维数组，同样可以通用numpy数组的函数和方法，
而且还具有其他灵活应用，后续会介绍到。
## 1.1 Series的创建
序列的创建主要有三种方式
# 1.1.1 通过一维数组创建序列
arr1 = np.arange(2, 10)
s1 = pd.Series(arr1)
# 1.1.2 通过字典的方式创建序列
dic1 = {'a': 10,'b': 20,'c': 30,'d': 40,'e': 50}
s2 = pd.Series(dic1)
# 通过DataFrame的某一行或某一列创建序列
举例在DataFrame的使用中讲
============================
## 1.2 DataFrame的创建
数据框的创建主要有三种方式：
# 1.2.1 通过二维数据创建数据框
arr2 = np.array(np.arange(12).reshape(4, 3))
df1 = pd.DataFrame(arr2)
# 1.2.2 通过字典的方式创建数据框
dic2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12],
        'd': [13, 14, 15, 16]}
df2 = pd.DataFrame(dic2)
==
dic2 = {'one': {'a': 1, 'b': 2, 'c': 3, 'd': 4},
        'two': {'a': 5, 'b': 6, 'c': 7, 'd': 8},
        'three': {'a': 9, 'b': 10, 'c': 11, 'd': 12}}
df2 = pd.DataFrame(dic2)
# 1.2.3 通过数据框的方式创建数据框，注意不同方式的类型
两对中括号内值可以多个或单个，类型为DataFrame
df4 = df2[['one', 'three']] # <class 'pandas.core.frame.DataFrame'> 必须为两对中括号
一对中括号中只能有一个值，类型为Series，多了报错KeyError
s3 = df2['one']     # <class 'pandas.core.series.Series'>

## 二、 数据索引index
不论是序列也好，还是数据框也好，对象的最左边总有一个非原始数据对象，这个是什么呢？不错，就是我们接下来要介绍的索引。
序列或数据框的索引有两大用处，一个是通过索引值或索引标签获取目标数据，
另一个是通过索引，可以使序列或数据框的计算、操作实现自动化对齐，下面我们就来看看这两个功能的应用
# 2.1 通过索引值或索引标签获取数据
s4 = pd.Series(np.array([1, 1, 2, 3, 5, 8]))
print(s4)
# indexSeries中的关键字参数，但是也可以如下写法：
s4.index = ['a', 'b', 'c', 'd', 'e', 'f']   # 添加额外的索引，默认的数字索引也是生效的
print(s4)
print(s4[4])    # 打印索引为4的值
print(s4['e'])  # 打印索引为e的值
print(s4[[1, 3, 5]])    # 打印指定序列，类似键值对(注意两对中括号)
# 注意切片形式，用冒号，不能使用print(s4['b','e'])
print(s4[:4])   # 也可以列表切片，输出对应序列，类似键值对
print(s4['b':'e'])
注意：如果通过索引标签获取数据的话，末端标签所对应的值是可以返回的！在一维数组中，就无法通过索引标签获取数据，这也是序列不同于一维数组的一个方面
# 2.2 自动化补齐
如果有两个序列，需要对这两个序列进行算术运算，这时索引的存在就体现的它的价值了—自动化对齐
s5 = pd.Series(np.array([10, 15, 20, 30, 55, 80]),
               index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s5)
s6 = pd.Series(np.array([12, 11, 13, 15, 14, 16]),
               index=['a', 'c', 'g', 'b', 'd', 'f'])
print(s6)
print(s5+s6)
print(s5/s6)
由于s5中没有对应的g索引，s6中没有对应的e索引，所以数据的运算会产生两个缺失值NaN;
这里的算术结果就实现了两个序列索引的自动对齐，而非简单的将两个序列加总或相除。
对于数据框的对齐，不仅仅是行索引的自动对齐，同时也会自动对齐列索引（列标签）
数据框中同样有索引，而且数据框是二维数组的推广，所以其不仅有行索引，而且还存在列索引，
关于数据框中的索引相比于序列的应用要强大的多，这部分内容将放在数据查询中讲解
## 三、 利用pandas查询数据
这里的查询数据相当于R语言里的subset功能，可以通过布尔索引有针对的选取原数据的子集、指定行、指定列等。我们先导入一个student数据集：
student = pd.read_csv('C:\\Users\\admin\\Desktop\\student.csv')
# 默认查询数据的前5行或末尾5行
student.head()
student.tail()
# 查询指定行
student.loc[[0,2,4,5,7]] # 这里的ix索引标签函数必须是中括号[]，多个行必须使用双重中括号
# 查询指定列
student[['Name','Height','Weight']].head() # 如果多个列的话，必须使用双重中括号
以上是从行或列的角度查询数据的子集，现在我们来看看如何通过布尔索引实现数据的子集查询
# 查询所有女生的信息
student[student['Sex']=='F']
# 查询出所有18岁以上的女生信息
student[(student['Sex']=='F') & (student['Age']>18)]
# 查询出所有18岁以上的女生姓名、身高和体重
student[(student['Sex']=='F') & (student['Age']>18)][['Name','Height','Weight']]
## 四、统计分析
pandas模块为我们提供了非常多的描述性统计分析的指标函数，如总和、均值、最小值、最大值等
print(np.random.seed(1234))
d1 = pd.Series(2 * np.random.normal(size=100) + 3)
d2 = np.random.f(2, 4, size=100)
d3 = np.random.randint(1, 100, size=100)
print(d1, d2, d3, sep='\n\n')
d1.count() #非空元素计算
d1.min() #最小值
d1.max() #最大值
d1.idxmin() #最小值的位置，类似于R中的which.min函数
d1.idxmax() #最大值的位置，类似于R中的which.max函数
d1.quantile(0.1) #10%分位数
d1.sum() #求和
d1.mean() #均值
d1.median() #中位数
d1.mode() #众数
d1.var() #方差
d1.std() #标准差
d1.mad() #平均绝对偏差
d1.skew() #偏度
d1.kurt() #峰度
d1.describe() #一次性输出多个描述性统计指标
一些属性
- a_list = list(employees['Full Name'].values)
# 不用转换成list，直接可以取值，类型：class 'pandas.core.series.Series'
ser_list = employees['Full Name'].values
print(ser_list[0])
print(a_list)
print(type(a_list))
print(employees.loc[1].values)
print(employees.index)
print(employees.index.any())
print(employees.index.values)
print(type(employees.index))
print(employees.index.shape)

