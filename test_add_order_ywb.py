#-*- coding: utf-8 -*-
'''
testcase_for_FSD_login   
3.x
'''

import string
import json
import sys
from common.basic_http import * 
from conf import server_config as device
from conf import api_url as api
import time
import datetime
import os

from  data import Flyuser_testdata as flyuser
from  data import System_Management_testdata as sysuser
from  data import Ywb_testdata as ywbuser
from  data import Mendian_testdata as mduser

from common.FSD_UserLogin import FSDLogin

my_obj = FSDLogin()

#ywb
ywblogindata=ywbuser.testdata_YWB_login_userdata_001
ywbsalesmanquerydata=ywbuser.testdata_YWB_salesmanquery_data_001
ywb_phone=ywblogindata['phone']
ywb_addorder_data=ywbuser.testdata_ywb_addorder_001
#ywb_addorder_data=ywbuser.payload

#mendian
userinfodata=mduser.testdata_MD_getwxuser_data_001




#case1--用户登录  
#--------------------------------------------------------      
def test_ywb_login(data):

    #调用登录
    ret=my_obj.ywb_login(data)
    if ret[0]!=0:
        token=ret[2]
        accountId=ret[1]

        return token,accountId
    else:
        print('error')
        return "error"

#--------------------------------------------------------  
#case2--salesmanquery
def test_ywb_salesmanquery(userid,token,data,phone):   
    ret=my_obj.ywb_salesmanquery(userid,token,data,phone)
    if ret!=1:
        print('error')
        return "error"

#--------------------------------------------------------  
#case3--addorder
def test_ywb_addorder(userid,token,phone,data):   
    ret=my_obj.ywb_addorder(userid,token,phone,data)
    if ret[0]!=0:
        token=ret[1]
        accountId=ret[0]
        
        return token,accountId
    else:
        print('error')
        return "error"
   
#--------------------------------------------------------  
def test_md_getwxuserinfo(data):

    #调用登录
    ret=my_obj.mendian_getwxuserinfo(data)
    if ret[0]!=0:
        return ret
    else:
        print('error')
        return "error"






#--------------------------------------------------------     
if __name__ == "__main__" :
    
    #data
    '''
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
    '''
    #mendian getwxuserinfo
    result=test_md_getwxuserinfo(userinfodata)
    if result!='error':
        userid=result[1]
        token=result[0]
    
    
    

    

  

    
      

