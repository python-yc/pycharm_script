class Person:
    # 不要使用这种方法，要不想传第一个参数，就使用静态方法
    def normal_method():
        print('normal')

    # 实例方法，不可以直接使用类名去调用；即需要实例化调用
    def method(self):
        print("{}'s method######".format(self))

    @classmethod
    def class_method(cls):
        print('class = {0.__name__} ({0})'.format(cls))
        cls.HEIGHT = 170

    @staticmethod
    def static_method():
        print(Person.HEIGHT)

print('~~~~类访问')
print(1,Person.normal_method()) # 可以吗 ：可以
#print(2,Person.method()) #可以吗 ：不可以（不能直接使用类访问实例方法）
print(3,Person.class_method()) # 可以吗 ：可以
print(4,Person.static_method()) # 可以吗 ：可以
print(Person.__dict__)
print('~~~类实例访问')
print('tom-----')
tom = Person()
#print(1,tom.normal_method()) #可以吗 ：不可以（不可以使用实例访问无修饰、无self的方法）
print(2,tom.method()) #可以吗 ：可以
print(3,tom.class_method()) #可以吗 ：可以
print(4,tom.static_method()) #可以吗 ：可以

