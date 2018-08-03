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
from common.FSD_UserLogin import FSDLogin
from modules.FSD_ReserveOrder_module import *
from  data import readtxt 

from  data import Ywb_testdata as ywbuser
from  data import Mendian_testdata as mduser

my_obj = FSDLogin()

#sys
syslogindata=sysuser.testdata_system_login_userdata_001
#ordernumber=sysuser.testdata_001_query_ordernumber
queryassginflyuser=sysuser.testdata_sys_query_assignflyuser_001
assignflyuser=sysuser.testdata_sys_assign_flyuser_001
#fsd
flyuserdata=flyuser.testdata_FSD_login_userdata_002
flyuser_msgdata=flyuser.testdata_FSD_messege_data_001
updateorderdata=flyuser.testdata_FSD_updateorderstate_001
submitorderdata=flyuser.testdata_FSD_updateorderreport_001
#ywb
ywblogindata=ywbuser.testdata_YWB_login_userdata_001
ywbsalesmanquerydata=ywbuser.testdata_YWB_salesmanquery_data_001
ywb_phone=ywblogindata['phone']
ywb_addorder_data=ywbuser.testdata_ywb_addorder_001
formaltypelist=ywbuser.ywb_formalType_list


#mendian
userinfodata=mduser.testdata_MD_getwxuser_data_001



#case1--用户登录  
#--------------------------------------------------------      
def test_sys_mangement_login(data):

    #调用登录
    ret=my_obj.system_management_login(data)
    if ret[0]!=0:
        farmtoken=ret[1]
        #print(farmtoken)
        return farmtoken
    else:
        print('error')
        return "error"

#--------------------------------------------------------  
#case2--sysMagement queryorderlist
def test_sys_queryorderlist(token,ordernumber):   
    ret=my_obj.sys_queryorderlist(token,ordernumber)
    if ret[0]!=0:
        order_id=ret[1]
        return order_id
    else:
        print('error')
        return "error"
    
#--------------------------------------------------------  
#case3--sysMagement queryassignflyuser
def test_sys_queryassignflyuser(token,order_id,phone,data):   
    ret=my_obj.sys_queryassignflyuser(token,order_id,phone,data)
    if ret[0]!=0:
        order_id=ret[1]
        return order_id
    else:
        print('error')
        return "error"
    
#--------------------------------------------------------  
#case4--sysMagement assignflyuser
def test_sys_publishorder(token,order_id,order_number,flyuser_id,data):   
    ret=my_obj.sys_publishorder(token,order_id,order_number,flyuser_id,data)
    if ret!=1:
        print('error')
        return "error"    
#--------------------------------------------------------        
#case5--fsd msg center
def test_fsd_msg_center(id,token,data):   
    ret=my_obj.fsd_msg_center(id,token,data)
    if ret[0]!=0:
        msgid=ret[1]
        text=ret[2]
        return msgid,text
    else:
        print('error')
        return "error"
#--------------------------------------------------------       
#case6--fsd orderproptquery
def test_fsd_orderpromptquery(ids,token,phone,msgid,ordernumber):   
    ret=my_obj.fsd_orderpromtquery(ids,token,phone,msgid,ordernumber)
    if ret!=1:
        print('error')
        return "error"  


#-------------------------------------------------
def test_fsd_updateorderstate(ids,token,phone,msg_id,ordernumber,data,order_text):
    ret=my_obj.fsd_updateorderstate(ids,token,phone,msg_id,ordernumber,data,order_text)
    if ret!=1:
        print('error')
        return "error"  

#-------------------------------------------------
def test_fsd_submitorder(ids,token,phone,msg_id,ordernumber,data,area):
    ret=my_obj.fsd_submitorder(ids,token,phone,msg_id,ordernumber,data,area)
    if ret!=1:
        print('error')
        return "error"  

#-------------------------------------------------
def test_fsd_orderboundquery(ids,token,phone,ordernumber):
    ret=my_obj.fsd_orderbundquery(ids,token,phone,ordernumber)
    if ret!=1:
        print('error')
        return "error"  




#case1--YWB 用户登录  
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
    else:
        return ret


#--------------------------------------------------------  
#case3--addorder
def test_ywb_addorder(userid,token,phone,data):   
    ret=my_obj.ywb_addorder(userid,token,phone,data)
    if ret[0]!=0:
        token=ret[1]
        
        return token
    else:
        print('error')
        return "error"




#--------------------------------------------------------  
    
if __name__ == "__main__" :
    
    #data
    '''
		
    #order_number=str(52941533266382634)  #派单，接单订单编号
    flyuser_phone='18301212965'   #派单飞手，接单飞手
    area=300   #actual a   #飞手提交作业亩数   
    
    formal_type=formaltypelist['normal']  #ywb正式订单
    #formal_type=formaltypelist['yanshi']   #ywb演示订单
    #formal_type=formaltypelist['test']   #ywb测试订单
    #formal_type=formaltypelist['longreserve']   #ywb长预约订单

    #print('formal-------------',formal_type)
    #print(ywb_addorder_data['formalType'])
    
    ywb_addorder_data['formalType']=formal_type
    if 	formal_type=='1':
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
    
    #sys assign order
    #------------------------sys
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

    result=test_sys_publishorder(token,order_id,order_number,flyuser_id,assignflyuser)

    '''
    '''
    #fsd  take order
    #--------------------------------------
    #5.fsd login
    flyuserdata['phone']=flyuser_phone
    
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
    print(order_text)
    result=test_fsd_updateorderstate(ids,token,flyuser_phone,msg_id,order_number,updateorderdata,order_text)



    #fsd submit order reportr
    #10.fsd submit order report

    #10提交作业报告
    time.sleep(10)
    '''
	
    '''
    #read data from txt file
    print('flyuser already take the order,now start submit the workresult..........\n')
    #ids=2187
    #msg_id=100000002682324
    #token="59c4a437c8084b4d8a0a1f90d2d28cfb"

    filename=os.getcwd()+'/data/flyuser_submit_order.txt'
    print("this is your orderdata filename:%s \n"%filename)
    
    lines=readtxt.read_from_txt(filename)
    res=readtxt.take_orderdata_from_readtxt(lines)
    readtxt.print_info(res)
    for i  in range(len(res)):
        ids=res[i]['ids']
        token=res[i]['token']
        msg_id=res[i]['msg_id']
        flyuser_phone=res[i]['flyuser_phone']
        order_number=res[i]['ordername']
        area=res[i]['area']    
        result=test_fsd_submitorder(ids,token,flyuser_phone,msg_id,order_number,submitorderdata,area)

        print(ids,flyuser_phone,token,order_number,msg_id,submitorderdata,area)

    '''
    
    #10.提交
    #result=test_fsd_submitorder(ids,token,flyuser_phone,msg_id,order_number,submitorderdata,area)

    
    
    
      

