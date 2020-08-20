#导包
import common.HTMLTestRunnerNew as HT
import requests
import unittest
import time
#设置一个用于装用例的容器
suite = unittest.TestSuite()
#设置一个发现用例的工具
load = unittest.defaultTestLoader
#用load取发现的用例
testcases = load.discover('test_cases',pattern='test*.py',top_level_dir=None)
#把发现的用例放在容器中
suite.addTests(testcases)
#设置测试报告的文档名---固定的名字reports+当前系统时间+HTML
currenttime = time.strftime("%Y-%m-%d %H-%M-%S")
filename = r'reports/reports_1'+currenttime+'.html'
with open(filename,'wb+') as fp:
    runner = HT.HTMLTestRunner(stream=fp,title='学生管理系统接口测试报告',description='hehehe',tester='wjx')
    runner.run(suite)

