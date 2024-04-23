#coding = utf-8
import unittest
import os

#大批量运行case文件
class RunCase(unittest.TestCase):
    def testcase01(self):
        #os.getcwd()获取工程当前路径,join拼接
        case_path = os.path.join(os.getcwd(),'case')
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    #执行所有case,执行顺序默认为字母/数字升序顺序执行，不想执行的通过skip装饰器跳过
    unittest.main()