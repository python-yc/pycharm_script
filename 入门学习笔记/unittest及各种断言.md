"""
单元测试：
要为函数编写测试用例，可先导入模块unittest以及要测试的函数，
再创建一个继承unittest.TestCase的类，
并编写一系列方法对函数行为的不同方面进行测试。
"""
模块名称不支持短横线，因此这里导入temporary-eg失败，暂时代码放在这

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    测试name_function.py
    
    def test_first_last_name(self):
        能够正确的处理像Janis Joplin 这样的姓名吗？
        formatted_name = ('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    
    def test_greet():
        content
unittest.main()

单元测试命名规范：
我们将这个方
法命名为test_first_last_name()，因为我们要核实的是只有名和姓的姓名能否被正确地格式化。
我们运行单元测试时，所有以test_打头的方法都将自动运行。
##如果每个测试用例都有重复代码的时候，可以通过使用unittest.TestCase类中的setUp()实现添加
##一次，然后每次都会被使用，同时对应的有个结尾的方法tearDown()

"""
##断言
- 基本断言方法
- 基本的断言方法提供了测试结果是True还是False。
- 所有的断言方法都有一个msg参数，如果指定msg参数的值，则将该信息作为失败的错误信息返回
序号	断言方法	断言描述
1	assertEqual(arg1, arg2, msg=None)	验证arg1=arg2，不等则fail
2	assertNotEqual(arg1, arg2, msg=None)	验证arg1 != arg2, 相等则fail
3	assertTrue(expr, msg=None)	验证expr是true，如果为false，则fail
4	assertFalse(expr,msg=None)	验证expr是false，如果为true，则fail
5	assertIs(arg1, arg2, msg=None)	验证arg1、arg2是同一个对象，不是则fail
6	assertIsNot(arg1, arg2, msg=None)	验证arg1、arg2不是同一个对象，是则fail
7	assertIsNone(expr, msg=None)	验证expr是None，不是则fail
8	assertIsNotNone(expr, msg=None)	验证expr不是None，是则fail
9	assertIn(arg1, arg2, msg=None)	验证arg1是arg2的子串，不是则fail
10	assertNotIn(arg1, arg2, msg=None)	验证arg1不是arg2的子串，是则fail
11	assertIsInstance(obj, cls, msg=None)	验证obj是cls的实例，不是则fail
12	assertNotIsInstance(obj, cls, msg=None)	验证obj不是cls的实例，是则fail




















