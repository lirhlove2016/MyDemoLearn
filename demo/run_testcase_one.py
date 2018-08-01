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
from testcase import test_one_case_demo as test_fsd

from conf.conf import *


#设置report_path
report_dir="/results/report/"
report_path=os.path.dirname(os.path.abspath(__file__)) + report_dir
print(report_path)

#手动设置
#report_path="D:\\workdtation\\workspace\\workspace\\FSD_test\\report\\"

#构造测试集
suite = unittest.TestSuite()
suite.addTest(test_fsd.TestFSD_Login('test_fsd_login'))


if __name__=='__main__':
    #执行测试
    #runner = unittest.TextTestRunner()
    #runner.run(suite)

    #报告
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    
    filename = report_path+now+'result.html'
    print(filename)
    
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'测试报告',
        description = u'用例的执行情况')
    
    runner.run(suite)
    fp.close()
