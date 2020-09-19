import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn("English",my_survey.responses)

    def test_store_single_response3(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        x = my_survey.responses[0]
        self.assertEqual("English",x)

"""
像这种每次都有重复代码的时候，可以通过使用unittest.TestCase类中的setUp()实现添加
一次，然后每次都会被使用，同时对应的有个结尾的方法tearDown
"""
'''
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    #每个单元用例开头都会用到的信息
    def setUp(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn("English",my_survey.responses)

    def test_store_single_response3(self):
        """测试单个答案会被妥善地存储"""
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        x = my_survey.responses[0]
        self.assertEqual("English",x)
        
    def tearDown(self):
        print("This test is over!")
'''

