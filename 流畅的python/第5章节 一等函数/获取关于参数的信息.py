# -*- coding: utf-8 -*-

"""
函数对象有个 __defaults__ 属性，它的值是一个元组，里面保存着定 位参数和关键字参数的默认值。
仅限关键字参数的默认值在 __kwdefaults__ 属性中。然而，参数的名称在 __code__ 属性中，它 的值是一个 code 对象引用，自身也有很多属性

为了说明这些属性的用途，如下：
"""

def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)


# 提取函数的签名 python3.5中
from inspect import signature

sig = signature(clip)
print('====')
print(sig)
print(str(sig))

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
