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
from testcase import test_FSD_submit_order_readdata as test_fsd_suborder
from testcase import test_SYS_assign_order_to_flyuser as test_sys_assignorder
from conf.conf import *



#设置report_path
report_dir="/results/report/"
report_path=os.path.dirname(os.path.abspath(__file__)) + report_dir
print(report_path)

#手动设置
#report_path="D:\\workdtation\\workspace\\workspace\\FSD_test\\report\\"

#构造测试集
suite = unittest.TestSuite()
#testcasefile.calssname(foo)



suite.addTest(test_sys_assignorder.TestSYS_assginOrder_to_flyuser('test_SYS_assignorder'))
suite.addTest(test_sys_assignorder.TestSYS_assginOrder_to_flyuser('test_fsd_take_order_from_msg'))


#suite.addTest(test_fsd_suborder.TestFSD_SubmitOrder('test_FSD_SubmitOrder_fromtxtdata'))


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
