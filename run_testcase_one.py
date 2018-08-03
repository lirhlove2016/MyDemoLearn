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

from testcase import test_one_case_demo as test_fsd
from testcase import test_FSD_submit_order_readtxt as test_fsd_suborder
from testcase import test_SYS_assign_order_to_flyuser as test_sys_assignorder
from testcase import test_ywb_addorder as test_addorder
from testcase import test_addassiginsubmit_order as test_addorder_takeorder

#设置report_path
report_dir="/results/report/"
report_path=os.path.dirname(os.path.abspath(__file__)) + report_dir
print(report_path)

#手动设置
#report_path="D:\\workdtation\\workspace\\workspace\\FSD_test\\report\\"

#构造测试集
suite = unittest.TestSuite()
#testcasefile.calssname(foo)

#业务宝下单
#suite.addTest(test_addorder.Test_addorder('test_ywb_add_order'))

#派单
#suite.addTest(test_sys_assignorder.Test_addorder_assginOrder_submitorder('test_SYS_assignorder'))
#接单
#suite.addTest(test_sys_assignorder.Test_addorder_assginOrder_submitorder('test_fsd_take_order_from_msg'))
#接单+提交作业报告
#suite.addTest(test_sys_assignorder.Test_addorder_assginOrder_submitorder('test_fsd_take_order_and_submit_order'))

#ywb下单 派单，接单，提交报告
suite.addTest(test_addorder_takeorder.Test_add_assgin_submit_order('test_addorder_and_submitrder'))



#提交作业报告（无协同）
#suite.addTest(test_fsd_suborder.TestFSD_SubmitOrder('test_FSD_submit_order_readtxt'))


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
        title = u'测试报告 测试环境',
        description = u'用例的执行情况')
    
    runner.run(suite)
    fp.close()
