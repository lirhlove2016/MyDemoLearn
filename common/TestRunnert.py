# coding=utf-8
'''
Created on:
@author: 
Project:编写测试用例
'''
import unittest
import time
import common.HTMLTestRunner as HTMLTestRunner
import os

from conf.conf import *

from common.logger import Logger
logger = Logger(logger="----TEST----").getlog()


class TestRunner(object):
    ''' Run test '''

    def __init__(self, cases="./",title="Auto API Test Report",description="Test case execution",report_dir="/results/report/",pattern='test*.py'):
        self.cases = cases
        self.title = title
        self.des = description
        self.reportDir=report_dir   #报告目录
        self.pattern=pattern        #匹配用例名    


    
    # 取test_case文件夹下所有用例文件
    def get_all_testsuite(self):
        testunit = unittest.TestSuite()

        # discover 方法定义
        discover = unittest.defaultTestLoader.discover(self.cases, pattern=self.pattern, top_level_dir=None)

        #discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
                print(testunit)
        return testunit

    def all_casenames(self):
        #获取所有执行用例集
        case_path=self.cases
        
        alltestnames =self.get_all_testsuite()       

        return alltestnames


    def run(self):
        logger.info("********TEST START********")
        suite=self.all_casenames()

        #取前面时间加入到测试报告文件名中
        now = time.strftime("%Y-%m-%d %M-%H_%M_%S", time.localtime(time.time()))

        filename = report_path+now+'result.html'
        print(filename)

        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=self.title, description=self.des)

        runner.run(suite)
        fp.close()
        logger.info("*********TEST END*********")



if __name__=='__main__':
    test=TestRunner()
    test.run()
    
    






    
