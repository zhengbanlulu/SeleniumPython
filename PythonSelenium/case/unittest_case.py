#coding = utf-8
import unittest

class FirstCase01(unittest.TestCase):
    #整体的前置条件，最先被执行
    @classmethod    #装饰器
    def setUpClass(cls):
        print('所有case的前置条件')

    #整体的后置条件，最后被执行
    @classmethod    #装饰器
    def tearDownClass(cls):
        print('所有case的后置条件')

    #每条case的前置条件
    def setUp(self):
        print("这是case的前置条件")

    #每条case的后置条件
    def tearDown(self):
        print("这是case的后置条件")

    #unittest测试函数必须以test开头，否则不会执行
    def testfirst01(self):
        print('这是第一条case')

    @unittest.skip("不执行第二条")
    def testfirst02(self):
        print('这是第二条case')

    def testfirst03(self):
        print('这是第三条case')

if __name__ == '__main__':
    #执行所有case,执行顺序默认为字母/数字升序顺序执行，不想执行的通过skip装饰器跳过
    unittest.main()

    '''
    #执行部分选择的case，执行顺序按照添加顺序执行
    suite = unittest.TestSuite()    #定义容器
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst01'))
    unittest.TextTestRunner().run(suite)
    '''