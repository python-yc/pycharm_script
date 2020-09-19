# 单下划线，双下划线都表示这些东西不要随便使用的提醒，不是不能访问，请遵守这些约定
# 单下划线是一种默认约定的，称为一种Python的一种规范
# 双下划线解释器会对其更改，单下划线不是对解释器的；通过下面两种方式查看
#print(Person.__dict__)
#print(p.__dict__)
class Person():
    def __init__(self,name,age=18):
        self.name = name
        self.__age = age

    def growup(self,incr=1):
        if 0 < incr < 150:
            self.__age += incr
    def getage(self):
        return self.__age

p = Person('tom')
# 私有变量不可以直接进行访问
#print(p.__age)
p.growup(2)

# 通过字典可以找私有变量在哪个地方，
# 反正就两个地方，不是类里面就是实例里面
print(Person.__dict__)
print(p.__dict__)   # 会发现在实例里面，然后可以进行调用

print(p._Person__age) # 但是可以这样的形式间接访问
# 再或者就是通过上面的方法进行返回值，然后调用
print(p.getage())

