# -*- coding: utf-8 -*-
"""
所有的映射类型在处理找不到的键的时候，都会牵扯到__missing__方法。这也是这个方法
称作“missing”的原因。虽然基类dict并没有定义这个方法，但是dict是知道有这么个东西
存在的。也就是说，如果有一个类继承了dict，然后这个继承类提供了__missing__方法，
那么在__getitem__碰到找不到的键的时候，Python就会自动调用它，而不是抛出一个KeyError异常
"""

"""
当有非字符串的键被查找的时候，StrKeyDict0是如何在该键不存在的情况下，把它转换为字符串的
"""

"""
像kinmy_dict.keys()这种操作在Python3中是很快的，而且即便映射类型对象很庞大也没关系。
这是因为dict.keys()的返回值是一个“视图”。视图就像一个集合，而且跟字典类似的是，在视图里查找一个元素的速度很快
"""

# isinstance(key,str)测试在上面的__missing__中是必需的
# __contains__方法在这里也是必需的；没有用更具Python风格的方式——k in my_dict——来检查键是否存在，也是必须的
# 想看具体解释在流畅的python中的  特殊方法__missing__ 中查看

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])

# print(d[1])     # KeyError: '1'
# print(d['1'])     # KeyError: '1'

print('================')
print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))

print('================')
print(2 in d)
print(1 in d)
