"""
题目：查找字符串。　　

程序分析：无。
"""
a = 'abcdefg'
b = 'abc'
c = 'd'
e = 'df'
print(a.find(b))
print("===============")
print(a.find(b,3,5))
print(a.find(c))
print(a.find(e))

help(str)
"""
 find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
"""