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

from  data import Flyuser_testdata as flyuser
from  data import System_Management_testdata as sysuser

from common.FSD_UserLogin import FSDLogin

from modules.test_FSD_ReserveOrder_module import *

my_obj = FSDLogin()

#data
flyuserdata=flyuser.testdata_FSD_login_userdata_001
password=flyuser.testdata_FSD_setpasswords_password
flyauth=flyuser.testdata_FSD_ahth
sysdata=sysuser.testdata_system_login_userdata_001
queryauth=sysuser.testdata_sys_query_auth_001
sysflyuserauth=sysuser.testdata_fly_user_auth_001 #实名认证
sysflyauth=sysuser.testdata_fly_auth_001  #飞手认证
flyuserteamdata=flyuser.testdata_create_flyuser_team_001
operatecardata=flyuser.testdata_FSD_add_operate_car_001

addplanedata=flyuser.testdata_flyuser_add_plane_001
queryCropPricedata=flyuser.testdat_queryCropPrice_data
reserveOrderdata=flyuser.testdata_addreserveOrder
headers=device.DICT__HTTP_HEADERS_002


def test_FSD_ReserveOrder():

    #step1:Random phone number
    phone=my_obj.ramdom_phone_number()
    print(phone)
    
    #step2:Fsd register
    datalist=my_obj.fsd_api_register(phone)
    print(datalist)
    if datalist[0]!=1:
        print('Fail')

    datalist=test_fsd_register(phone)

    #step3:Fsd set password
    token=datalist[1]
    ids=datalist[2]
    test_fsd_set_password(token,ids,phone,password)    



    #4:Fsd api login
    #phone='14433334003'    
    datalist=test_fsd_login(phone,flyuserdata)
    print(datalist)

    ids=datalist[2]
    token=datalist[1]
    

    #5:Fsd fly auth   
    test_fly_auth(ids,token,phone,flyauth)
    

    #6:Sys login    
        
    re=test_sys_mangement_login(sysdata)
    headers['FARMFRIEND_TOKEN']=re


    #7:query auth
    #phone='14145173089'
    datalist=test_query_fly_auth(phone,queryauth)
    flyuserid=datalist[1]
    
    
    #8:sys fly user auth 实名认证        
    test_sys_flyuser_auth(flyuserid,sysflyuserauth,headers)

    #9:sys fly auth
    #ids=2894
    flyUserId=ids
    
    datalist=test_sys_fly_auth(flyuserid,sysflyauth,headers)
    print(datalist)


    #10:create flyuser team
    ids=ids
    token=token
    test_create_flyuser_team(ids,token,flyuserteamdata)
    
    #11:add operate car
    
    test_add_operate_car(ids,token,operatecardata)
    
    #12:add plane
    userId=ids
    test_fsd_add_plane(phone,userId,token,addplanedata)

    #13:get plane id
    userId=ids
    re=test_get_plane_id(userId,token,phone)
    planeid=re[1]

    #14:update Xy   
    test_update_Xy(userId,token,phone)

    #15:get car id
    datalists=test_get_car_id(userId,token,phone)
    carid=datalists[1]

    #16:get reserve calendar 提取空闲时间
    print('get reserver calendar-------------------------') #失败了caiid long
    print(carid)
    datalist=test_get_reserve_calendar(userId,token,phone,carid)
    
    
    var1=int(datalist[1])
    var2=86400
    time1=var1+var2
    #print(time1)
    print(type(time1),time1)

    #17:query crop price  获取价格
    print('--------------------query crop price-------------------------')
        
    #time=[1525881600]  
    re=test_query_crop_price(ids,token,phone,queryCropPricedata,time1)
    print(re)

    #取最低价与最高价至今
    
    var1=float(re[0]) #最低价
    var2=float(re[1])  #最高价
    price1=var2*0.8
    
    #18:add reserve order
    print('--------------------add reserve order -------------------------')

    print(type(time1),time1)
    print(type(planeid),planeid)
    
    print(type(carid),carid)
    print(price1)
    
    re=test_add_reserve_order(ids,token,phone,carid,planeid,price1,time1,reserveOrderdata)
    

    

test_FSD_ReserveOrder()   
    
    
    

