# 无参数装饰器，函数本身是参数

def wrap(func):
    fun_list = []
    fun_list.append(func)

    def a(*args, **kwargs):
        print('running in a()')

        print('args:{}, kwargs:{}'.format(args, kwargs))
        if args:
            print('args here: %s' % args)
        if kwargs:
            print('kwargs here: %s' % kwargs)
        else:
            print('kwargs is None...')

        return fun_list
    return a


@wrap
def b():
    print('run in b')


# b()
a = 5
print(b(a))
print('===================')
rlt = b(a, name='xiaoming', age=18)
print('==')
print('rlt:', rlt)
print('===========================')
for f in rlt:
    f()


# 有参数装饰器

