# coding: utf-8

# tag 函数用于生成 HTML标签；使用名为 cls 的关键 字参数传入“class”属性，这是一种变通方法，
# 因为“ class”是 Python 的关键字
def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    # print(attrs)
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name)
                         for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print('====')
print(tag('p', 'hello', 'world'))

print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}

# print(*my_tag)
print(tag(**my_tag))


"""
仅限关键字参数是 Python 3 新增的特性。在示例 5-10 中，cls 参数只能 通过关键字参数指定，
它一定不会捕获未命名的定位参数。定义函数时 若想指定仅限关键字参数，要把它们放到前面
有 * 的参数后面。如果不 想支持数量不定的定位参数，但是想支持仅限关键字参数，在签名中放 一个 *
"""
def f(a, *, b):
    return a, b


# 放在 * 后，此时的 参数 b 必须指定，即为关键字参数了
print(f(1, b=2))
# TypeError: f() takes 1 positional argument but 2 were given
# print(f(1, 2))
'''注意，仅限关键字参数不一定要有默认值，可以像上例中 b 那样，强制 必须传入实参。'''
