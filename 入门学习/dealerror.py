# 简单异常例子
"""
#简单的一个循环判断，可以解决输入的数为非整数的问题
while True:
    try:
        x = int(input("请输入一个整数"))
    except ValueError as e:
        print(e)
        continue
    else:
        print("ok")
        print(x)
        break
"""

'''
#这个如果出错只是跳出，但是没有给出报错位置
import math
try:
    num = int(input("请输入一个数"))
    rst = math.trunc(100/num)
    print("计算结果是：{0}".format(rst))
    #print("计算结果是：%s" %rst)
except:
    print("wrong")
    #exit是退出程序的意思
    exit()
'''

import math
try:
    num = int(input("请输入一个数"))
    rst = math.trunc(100/num)
    print("计算结果是：{0}".format(rst))
#捕获异常，把异常实例化，出错信息会在实例化里
#注意以下写法
#以下语句是捕获ZeroDivisionError异常并实例化e,给出提示信息
#如果是多种error的情况，需要把越具体的错误，越往前放
except ZeroDivisionError as e:
    print("除0错误")
    print(e)
    #exit是退出程序的意思
    exit()
#except ValueError as e:
#    print("无效值")
#    print(e)
except NameError as e:
    print("名称未定义")
    print(e)

#有Exception异常后，就不需要在写基本异常情况了，这个是常规错误的基类
except Exception as e:
    print("我也不知道哪错了")
    print(e)

print(type(ZeroDivisionError))


#raise案例
#自定义异常，推荐是系统异常的子类（一般不用自定义）
#这样可以编写自己的错误信息代码
class DaNaValueError(ValueError):
    pass
try:
    print("I am studying python!")
    print(3.14)
    #手动引发一个异常
    #注意语法：raise ErrorClassName
    raise DaNaValueError
    print("还没完呀")
except NameError as e:
    print("NameEoor")
except DaNaValueError as e:
    print("DaNaValueError。。。。。")
except ValueError as e:
    print("ValueError。。。。。")
except Exception as e:
    print("没有异常")
finally:
    print("我肯定被执行的")




