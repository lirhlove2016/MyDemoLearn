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

from modules.Addorder_submitorder_module import *

from common.basic_http import * 

from conf import server_config as device
from conf import api_url as api

from  data import Flyuser_testdata as flyuser
from  data import System_Management_testdata as sysuser

from common.FSD_UserLogin import FSDLogin
my_obj = FSDLogin()

from testcase.test_ywb_md_addorder import Test_addorder
addorder_obj=Test_addorder()

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

#ordernumber=sysuser.testdata_001_query_ordernumber   #派单，接单订单编号
flyuser_phone=sysuser.testdata_001_flyuser_phone
area=sysuser.testdata_001_flyuser_submit_order_area




'''
数据部分  end
-----------
'''

class Test_add_assgin_submit_order(unittest.TestCase):
    
    """flyuser take order and submit order"""
	        
    def setUp(self):
        print('---------TEST START-------------')

    #1,YWB addorder and assignorder
    def test_ywb_addorder_and_submitrder(self):

        """flyuser take order and submit order"""
        
        formal_type=formaltypelist['normal']  #ywb正式订单
        #formal_type=formaltypelist['yanshi']   #ywb演示订单
        #formal_type=formaltypelist['test']   #ywb测试订单
        #formal_type=formaltypelist['longreserve']   #ywb长预约订单

	#print('formal-------------',formal_type)
	#print(ywb_addorder_data['formalType'])
        if  formal_type=='1':
            print('正在下单，业务宝-正式订单......')
        elif formal_type=='2':
            print('正在下单，业务宝-演示订单......')
        elif formal_type=='3':
            print('正在下单，业务宝-测试订单......')
        elif formal_type=='4':
            print('正在下单，业务宝-长预约订单......')
                        
        #1.ywb login    
        datalist=test_ywb_login(ywblogindata)
        print(datalist)
        userid=datalist[1]
        token=datalist[0]
        
        print(userid,token)

        #2.ywb salesmanquery
        result=test_ywb_salesmanquery(userid,token,ywbsalesmanquerydata,ywb_phone)

        #3add order
        #拜访人，不带药，不开发票
        result=test_ywb_addorder(userid,token,ywb_phone,ywb_addorder_data)
        if result!='error':
            order_number=result                     
        print('ywb add order-----------',order_number)

        #order_number="73781533228463687"

        #2.sys assign order to flyuser
        #step1:sys login   
        result=test_sys_mangement_login(syslogindata)
      
        #step2:queryorder of ordernumber
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
        #print('order_number',type(order_number),order_number)

        result=test_sys_publishorder(token,order_id,order_number,flyuser_id,assignflyuser)


        #3.flyuser take order and submit workreport
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
        result=test_fsd_orderpromptquery(ids,token,flyuser_phone,msg_id,order_number)
        
        #8.fsd updateorderstate //接单
        #确认接单
        time.sleep(1)
        #print(order_text)
        result=test_fsd_updateorderstate(ids,token,flyuser_phone,msg_id,order_number,updateorderdata,order_text)

        #9.orderboundquery
        result=test_fsd_orderboundquery(ids,token,flyuser_phone,order_number)
        #10.fsd submit order report
        #等待timeout=10s,
        time.sleep(10)
        
        print('------------this is your order info-------------------------')
        print('------------------------------------------------------------')
        print('ids,flyuser_phone,token,ordernumber,msg_id,submitorderdata,area')       
        print(ids,flyuser_phone,token,order_number,msg_id,submitorderdata,area)
        print('------------------------------------------------------------')
        
        result=test_fsd_submitorder(ids,token,flyuser_phone,msg_id,order_number,submitorderdata,area)
    
    def test_mendian_addorder_and_submit(self):
        #1.mendian addorder
        order_number=addorder_obj.test_md_add_order()
        
        #2.sys assign order to flyuser
        #step1:sys login   
        result=test_sys_mangement_login(syslogindata)
      
        #step2:queryorder of ordernumber
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
        #print('order_number',type(order_number),order_number)

        result=test_sys_publishorder(token,order_id,order_number,flyuser_id,assignflyuser)


        #3.flyuser take order and submit workreport
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
        result=test_fsd_orderpromptquery(ids,token,flyuser_phone,msg_id,order_number)
        
        #8.fsd updateorderstate //接单
        #确认接单
        time.sleep(1)
        #print(order_text)
        result=test_fsd_updateorderstate(ids,token,flyuser_phone,msg_id,order_number,updateorderdata,order_text)

        #9.orderboundquery
        result=test_fsd_orderboundquery(ids,token,flyuser_phone,order_number)
        #10.fsd submit order report
        #等待timeout=10s,
        time.sleep(10)
        
        print('------------this is your order info-------------------------')
        print('------------------------------------------------------------')
        print('ids,flyuser_phone,token,ordernumber,msg_id,submitorderdata,area')       
        print(ids,flyuser_phone,token,order_number,msg_id,submitorderdata,area)
        print('------------------------------------------------------------')
        
        result=test_fsd_submitorder(ids,token,flyuser_phone,msg_id,order_number,submitorderdata,area)
        

                              
        def tearDown(self):
            print('-------TEST END----------------- ')

if __name__ == '__main__':
    #unittest.main()  
    '''
    suite = unittest.TestSuite()
    #suite.addTest(TestOne("test_add"))
    #suite.addTest(Test_addorder("test_ywb_add_order"))
    suite.addTest(Test_add_assgin_submit_order("test_mendian_addorder_and_submit"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    
    

