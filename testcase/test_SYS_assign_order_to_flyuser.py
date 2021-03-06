#-*- coding: utf-8 -*-
'''
后台派单给飞手 
3.x
'''

import unittest
import string
import json
import sys
import time
import datetime
import os
from common import HTMLTestRunner
from  time  import sleep

from modules.FSD_ReserveOrder_module import *
from modules.Addorder_submitorder_module import *

from common.basic_http import * 

from conf import server_config as device
from conf import api_url as api

from  data import Flyuser_testdata as flyuser
from  data import System_Management_testdata as sysuser

from common.FSD_UserLogin import FSDLogin
from  data import readtxt 

from testcase.test_ywb_md_addorder import Test_addorder

my_obj = FSDLogin()

'''
数据部分  start
------------------
'''
#data
#sys
syslogindata=sysuser.testdata_system_login_userdata_001
queryassginflyuser=sysuser.testdata_sys_query_assignflyuser_001
assignflyuser=sysuser.testdata_sys_assign_flyuser_001

#fsd
flyuserdata=flyuser.testdata_FSD_login_userdata_002
flyuser_msgdata=flyuser.testdata_FSD_messege_data_001
updateorderdata=flyuser.testdata_FSD_updateorderstate_001
submitorderdata=flyuser.testdata_FSD_updateorderreport_001

ordernumber=sysuser.testdata_001_query_ordernumber   #派单，接单订单编号
flyuser_phone=sysuser.testdata_001_flyuser_phone
area=sysuser.testdata_001_flyuser_submit_order_area

'''
数据部分  end
-----------
'''

class Test_addorder_assginOrder_submitorder(unittest.TestCase):
    """systemManegement assign order to flyuserr"""
	        
    def setUp(self):
        print('---------TEST START-------------')

    #case1--sys 派单给飞手
    def test_SYS_assignorder(self):
        #sys assign order
        #------------------------sys
        #step1:sys login   
        result=test_sys_mangement_login(syslogindata)
        
        #step2:queryorder of irdernumber
        if result!='error':
            token=result
        print(token)
       
            
        result=test_sys_queryorderlist(token,ordernumber)
        if result!='error':
            order_id=result

        #step3:select assign flyuser
        result=test_sys_queryassignflyuser(token,order_id,flyuser_phone,queryassginflyuser)
        if result!='error':
            flyuser_id=result

        print(flyuser_id)
        
        #step4:publish flyuser
        print('flyuserid type',type(flyuser_id),flyuser_id)
        result=test_sys_publishorder(token,order_id,ordernumber,flyuser_id,assignflyuser)
    
    #2:take order
    def test_fsd_take_order_from_msg(self):
        """flyuser take order"""		
        datalist=test_fsd_login(flyuser_phone,flyuserdata)
        print(datalist)

        ids=datalist[2]
        token=datalist[1]

        #6.fsd order messege
        #fsd 首页消息       
        print(flyuser_msgdata)
        result=test_fsd_msg_center(ids,token,flyuser_msgdata)
        
        if result!='error':
            msg_id=result[0]
            order_text=result[1]

        #7.fsd orderprompt
        #点击接单的弹窗
        time.sleep(5)
        result=test_fsd_orderpromptquery(ids,token,flyuser_phone,msg_id,ordernumber)
        
        #8.fsd updateorderstate //接单
        #确认接单
        time.sleep(1)
        #print(order_text)
        result=test_fsd_updateorderstate(ids,token,flyuser_phone,msg_id,ordernumber,updateorderdata,order_text)

        #9.orderboundquery
        result=test_fsd_orderboundquery(ids,token,flyuser_phone,ordernumber)

        return ids,token,msg_id

    #3,take order and submit order 
    def test_fsd_take_order_and_submit_order(self):
        """flyuser take order and submit order"""
        
        ids,token,msg_id=self.test_fsd_take_order_from_msg()      
        #10.fsd submit order report
        #等待timeout=10s,
        time.sleep(10)
        
        print('------------this is your order info-------------------------')
        print('------------------------------------------------------------')
        print('ids,flyuser_phone,token,ordernumber,msg_id,submitorderdata,area')       
        print(ids,flyuser_phone,token,ordernumber,msg_id,submitorderdata,area)
        print('------------------------------------------------------------')
        
        result=test_fsd_submitorder(ids,token,flyuser_phone,msg_id,ordernumber,submitorderdata,area)

    #4,YWB addorder and assignorder
    def test_addorder_and_submitrder(self):
        """flyuser take order and submit order"""
        #1.ywb addorder
        ywblogin=Test_addorder()
        order_number=ywblogin.test_ywb_add_order()

        #2.sys assign order to flyuser
        #sys assign order
        #step1:sys login   
        result=test_sys_mangement_login(syslogindata)
        
        #step2:queryorder of irdernumber
        if result!='error':
            token=result
        print(token)
       
            
        result=test_sys_queryorderlist(token,order_number)
        if result!='error':
            order_id=result

        #step3:select assign flyuser
        result=test_sys_queryassignflyuser(token,order_id,flyuser_phone,queryassginflyuser)
        if result!='error':
            flyuser_id=result

        print(flyuser_id)        
        #step4:publish flyuser
        print('flyuserid type',type(flyuser_id),flyuser_id)
        result=test_sys_sys_publishorder(token,order_id,order_number,flyuser_id,assignflyuser)

        #3.flyuser take order and submit workreport
        self.test_fsd_take_order_and_submit_order()

        
        
        
        
        
                               
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

    
    

