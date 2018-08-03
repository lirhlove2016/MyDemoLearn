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
from common.basic_http import * 

from conf import server_config as device
from conf import api_url as api

from  data import Flyuser_testdata as flyuser
from  data import System_Management_testdata as sysuser
from  data import Ywb_testdata as ywbuser
from  data import Mendian_testdata as mduser

from common.FSD_UserLogin import FSDLogin

my_obj = FSDLogin()

'''
数据部分  start
------------------
'''
#ywb
ywblogindata=ywbuser.testdata_YWB_login_userdata_001
ywbsalesmanquerydata=ywbuser.testdata_YWB_salesmanquery_data_001
ywb_phone=ywblogindata['phone']
ywb_addorder_data=ywbuser.testdata_ywb_addorder_001
#ywb_addorder_data=ywbuser.payload

#mendian
openid=mduser.testdata_mendian_login_openid[0]
userinfodata=mduser.testdata_MD_getwxuser_data_001
mdaddorderdata=mduser.testdata_md_addorder_001
getvoucherdata=mduser.testdata_md_getcanuservoucher_001
getfullareamsg=mduser.testdata_md_getfullareamsg_001
getbalancedata=mduser.testdata_md_getbalance_001
orderprepaydata=mduser.testdata_md_orderprepay_001


'''
数据部分  end
-----------
'''

class Test_addorder(unittest.TestCase):
    """ywb add order"""
	    
    
    def setUp(self):
        print('---------TEST START-------------')

    #case1--ywb add order
    def test_ywb_add_order(self):
        """ywb add order"""
        #step1:ywb login   
        ret=my_obj.ywb_login(ywblogindata)
        if ret[0]!=0:
            token=ret[2]
            accountId=ret[1]
        else:
            print('error')

        #2.ywb salsmanquery
        userid=accountId
        ret=my_obj.ywb_salesmanquery(userid,token,ywbsalesmanquerydata,ywb_phone)
        if ret!=1:
            print('error')
            return "error"


        #step3:ywb add order
        #拜访人，不带药，不开发票
        ret=my_obj.ywb_addorder(userid,token,ywb_phone,ywb_addorder_data)
        if ret[0]==1:
            order_numbe=ret[1]       
        else:
            print('error')
    
    #case2--mendian add order
    def test_md_add_order(self):
        """mend add order"""

        #1.mendian getwxuserinfo
        ret=my_obj.mendian_getwxuserinfo(userinfodata,openid)
        if ret[0]==1:
            userid=ret[2]
            token=ret[1]
        else:
            print('error')
        #2.mendian addorder
        
        ret=my_obj.mendian_addorder(token,userid,mdaddorderdata)
        if ret[0]==1:
            prepayid=ret[1]
            groupmembercount=ret[2]
            preferentlist=ret[3]
            
        #3.mendian getcanuservoucher        
        pretotalprice=preferentlist[groupmembercount-1]['showMoney']
        prepaypercent=preferentlist[groupmembercount-1]['prePayPercent']

        ret=my_obj.mendian_getcanuservoucher(token,userid,prepayid,pretotalprice,prepaypercent,getvoucherdata)
        if ret[0]==1:
            vouchlist=ret[1]
        vouponcode=vouchlist[0]['couponCode']
        
        #4.mendian getfullareamsg     
        ret=my_obj.mendian_getfullareamsg(token,userid,prepayid,getfullareamsg)
        if ret[0]==1:
            fullareastate=ret[1]
            fullareamsg=ret[2]
        
        #5.mendian getbalance
        ret=my_obj.mendian_getbalance(token,userid,getbalancedata)
        if ret[0]==1:
            amount=ret[1]
                    
    
        #6.mendian orderprepay
        orderprepaydata
        chekcode='1234'
        ret=my_obj.mendian_orderprepay(token,userid,prepayid,pretotalprice,prepaypercent,chekcode,openid,orderprepaydata)
        if ret[0]==1:
            order_number=ret[1]
        return order_number
        
        
    def tearDown(self):
            print('-------TEST END----------------- ')

if __name__ == '__main__':
    #unittest.main()
    
    suite = unittest.TestSuite()
    #suite.addTest(TestOne("test_add"))
    #suite.addTest(Test_addorder("test_ywb_add_order"))
    suite.addTest(Test_addorder("test_md_add_order"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


    
    

