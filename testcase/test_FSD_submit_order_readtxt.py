#-*- coding: utf-8 -*-
'''
飞手提交作业报告 
3.x
'''

import unittest
import string
import json
import time
import datetime
import os
from common import HTMLTestRunner
from  time  import sleep

import sys
from common.basic_http import * 

from conf import server_config as device
from conf import api_url as api

from modules.FSD_ReserveOrder_module import *
from modules.SYS_FSD_submit_order import *

from  data import Flyuser_testdata as flyuser
from  data import System_Management_testdata as sysuser

from common.FSD_UserLogin import FSDLogin
from  data import readtxt 

my_obj = FSDLogin()

#data
#fsd
flyuserdata=flyuser.testdata_FSD_login_userdata_002
flyuser_msgdata=flyuser.testdata_FSD_messege_data_001
updateorderdata=flyuser.testdata_FSD_updateorderstate_001
submitorderdata=flyuser.testdata_FSD_updateorderreport_001

filename=os.getcwd()+'/data/flyuser_submit_order.txt'
print("this is your orderdata filename:%s \n"%filename)

class TestFSD_SubmitOrder(unittest.TestCase):
    """fsd SubmitOrderwork"""
    
    def setUp(self):
        print('---------TEST START-------------')


    #case1--FSD提交作业报告
    def test_FSD_SubmitOrder_fromtxtdata(self):
        time.sleep(5)
       
        print('flyuser already take the order,now start submit the workresult..........\n')       
        #frm file read datas
        lines=readtxt.read_from_txt(filename)
        res=readtxt.take_orderdata_from_readtxt(lines)
        readtxt.print_info(res)
        for i  in range(len(res)): 
            #ids=res[i]['ids']
            #token=res[i]['token']

            #ids,token from login
            msg_id=res[i]['msg_id']
            flyuser_phone=res[i]['flyuser_phone']
            order_number=res[i]['ordername']
            area=res[i]['area']

             #1.飞手登录，提取token,userid
            datalist=test_fsd_login(flyuser_phone,flyuserdata)
            #print(datalist)
            
            ids=datalist[2]
            token=datalist[1]
                   
            #2.flyuser submit order
            print(ids,flyuser_phone,token,order_number,msg_id,submitorderdata,area) 
            result=test_fsd_submitorder(ids,token,flyuser_phone,msg_id,order_number,submitorderdata,area)
                   
    
    def tearDown(self):
            print('-------TEST END----------------- ')


if __name__ == '__main__':
    #unittest.main()  
    # 1、构造用例集
    suite = unittest.TestSuite()
    # 2、执行顺序是安加载顺序：先执行test_sub，再执行test_add
    suite.addTest(TestFSD_ReserveOrder("test_FSD_ReserveOrder"))
    #suite.addTest(TestOne("test_add"))
    # 3、实例化runner类
    runner = unittest.TextTestRunner()
    # 4、执行测试
    runner.run(suite)

    
    

