# -*- coding: utf-8 -*-
import sys

# https://www.cnblogs.com/wf-linux/archive/2018/08/01/9400354.html

print(sys.modules.keys())
print(sys.hexversion)
print(sys.version)

'''
sys.stdin,sys.stdout,sys.stderr

stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满
足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 
或者以非标准的方式处理它们.
我们常用print和raw_input来进行输入和打印，那么print 和 raw_input是如何与标准输入/输出流建立关系的呢？
其实Python程序的标准输入/输出/出错流定义在sys模块中，分别 为： sys.stdin,sys.stdout, sys.stderr
'''
print('=====sys.std=======')
sys.stdout.write('hello world!')
print('please enter yourname:')
name = sys.stdin.readline()[:-1]
print('hi, %s' % name)


"""
sys.argv 命令行参数List，第一个元素是程序本身路径

sys.modules.keys() 返回所有已经导入的模块列表

sys.exc_info() 获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息

sys.exit(n) 退出程序，正常退出时exit(0)

sys.hexversion 获取Python解释程序的版本值，16进制格式如：0x020403F0

sys.version 获取Python解释程序的版本信息

sys.maxint 最大的Int值

sys.maxunicode 最大的Unicode值

sys.modules 返回系统导入的模块字段，key是模块名，value是模块

sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值

sys.platform 返回操作系统平台名称

sys.stdout 标准输出

sys.stdin 标准输入

sys.stderr 错误输出

sys.exc_clear() 用来清除当前线程所出现的当前的或最近的错误信息

sys.exec_prefix 返回平台独立的python文件安装的位置

sys.byteorder 本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'

sys.copyright 记录python版权相关的东西

sys.api_version 解释器的C的API版本
"""
