# -*- coding: utf-8 -*-
"""
可选参数可以有默认值，这是 Python 函数定义的一个很棒的特性，
这样 我们的 API 在进化的同时能保证向后兼容。然而，我们应该避免使用可 变的对象作为参数的默认值。
"""
"""passengers 的默认值不是 None，而是 []，这样就不用像之前那 样使用 if 判断了。这个“聪明的举动”会让我们陷入麻烦"""
class HauntedBus:
    """备受幽灵乘客折磨的校车"""
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

# 此时就会发现 bus3 实例会有bus2 的值，原因就是可变对象作为默认值导致的
bus3 = HauntedBus()
print(bus3.passengers)

print(bus3.passengers is bus2.passengers)

"""
这种问题很难发现。以上示例所示，实例化 HauntedBus 时，如果 传入乘客，会按预期运作。
但是不为 HauntedBus 指定乘客的话，奇怪 的事就发生了，这是因为 self.passengers 
变成了 passengers 参数 默认值的别名。出现这个问题的根源是，默认值在定义函数时计算
（通 常在加载模块时），因此默认值变成了函数对象的属性。因此，如果默 认值是可变对象，
而且修改了它的值，那么后续的函数调用都会受到影 响。

# 因此预防可变参数，将以上__init__函数修改为None为默认参数：
def __init__(self, passengers=None): 
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers)

此外，这种处理方式还更灵活：现在，传给 passengers 参数的值可以 是元组或任何其他可迭代对象
"""
