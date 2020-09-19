'''
题目：列表使用实例。

程序分析：无。
'''
# list
# 新建列表
testList = [10086,'zhongguoyidong',[1,2,3,4]]

# 访问列表长度
print(len(testList))
# 到列表结尾
print(testList[1:])
# 向列表添加元素
testList.append('i\'m new here!')

print(len(testList))
print(testList[-1])
# 弹出列表的最后一个元素
print(testList.pop())
print(len(testList))
print(testList)



