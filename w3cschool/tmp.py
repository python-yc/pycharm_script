def f():
    c = 1

    def fa():
        d = c + 1
        return d

    return fa

a = f()
print(type(a))
print(a())


def f():
    c = 1

    def fa():
        c = c + 1
        return c

    return fa

a = f()
