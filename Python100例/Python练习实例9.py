"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""
#coding:utf-8
import time

myD = {1:'a',2:'two',3:'three'}
for key , value in myD.items():
    print(key,'---',value)
    time.sleep(1)

