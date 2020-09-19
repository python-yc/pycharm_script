import unittest
from city_coutry import get_formatted_information

#get_formatted_information('an','china')

class NameTestCase(unittest.TestCase):
    #setUp与tearDown可以不使用，如果，每条用例都会分配一对
    #单元测试用例不是按你写的顺序执行，而是按字母排序而执行
    def setUp(self):
        print("Starting...")
    def test_city_country(self):
        formatted_name = get_formatted_information('anhui','china')
        self.assertEqual(formatted_name,"Anhui,China")

    def test_city_country2(self):
        formatted_name = get_formatted_information('安徽', 'china')
        self.assertEqual(formatted_name, "安徽,China")

    def test_city_country2(self):
        formatted_name = get_formatted_information('nanjing', 'china')
        self.assertEqual(formatted_name, "Nanjing,,China")
    def tearDown(self):
        print("Ending...")

#unittest.main()


