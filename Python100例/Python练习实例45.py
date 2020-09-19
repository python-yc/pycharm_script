"""
两个 3 行 3 列的矩阵，
实现其对应位置的数据相加，并返回一个新矩阵：

程序分析：创建一个新的 3 行 3 列的矩阵，
使用 for 迭代并取出 X 和
Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
"""
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[0,0,0],
     [0,0,0],
     [0,0,0]]

# 迭代输出行
for i in range(len(x)):
    # 迭代输出列
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

print(result)
print(*result)
for r in result:
    print(r)
print("==============")
for r in result:
    print(*r)