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


my_obj = FSDLogin()
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



#case1--FSD用户登录
#--------------------------------------------------------  
def test_fsd_login(phone,userdata):
    datalist=[]
    #返回值
    datalist=my_obj.fsd_api_login(phone,userdata)
    #print(datalist)
    
    if datalist[0]!=1:
        print('fail')
        return None
    else:
        #token=datalist[1]
        #userid=datalist[2]
        #print(token,userid)
        return datalist
    
    
#--------------------------------------------------------      
#case2--sysMagement用户登录
def test_sys_mangement_login(data):

    #调用登录
    ret=my_obj.system_management_login(data)

    if ret[0]!=0:
        farmtoken=ret[1]
        #print(farmtoken)
        
        return farmtoken
    else:
        print('error')
        return ret

#--------------------------------------------------------  
#case3--sysMagement冻结飞手
def test_sys_management_freez_flyuser(userid,token):
    #userid=2803
    #my_obj = FSDLogin()    
    my_obj.sysment_management_freeze_flyuser(userid,token)
    

#--------------------------------------------------------      
def test_take_random_phonenumber():
    phone=my_obj.ramdom_phone_number()
    print(phone)
    return phone

#--------------------------------------------------------  
#case4----FSD用户注册
def test_fsd_register(phone):
    #phone='19933332222'   
    datalist=my_obj.fsd_api_register(phone)
    print(datalist)
    if datalist[0]!=1:
        print('Fail')

    return datalist

#--------------------------------------------------------  
#case5--FSD设置密码
def test_fsd_set_password(token,ids,phone,password):
    #password=flyuser.testdata_FSD_setpasswords_password
    flag=my_obj.flyuser_set_password(token,ids,phone,password)

    if flag!=1:
        print('Fail')
    return flag


# 不用了 
#--------------------------------------------------------  
def take_idandtoken_from_fsdlogin(fsdobj,userdata):
    my_obj=fsdobj
    datalist=my_obj.fsd_api_login(userdata)
    print(datalist)
    
    #成功后，设置密码
    if datalist[0]==1:
        #print(datalist[1])
        token=datalist[1].strip('\"')
        ids=datalist[2]
        status=1
        return  status,ids,token
    else:
        status=0
        return status

#--------------------------------------------------------  
def take_idandtoken_from_syslogin(fsdobj,userdata):
    my_obj=fsdobj
    datalist=my_obj.fsd_api_login(userdata)
    print(datalist)
    
    #成功后，设置密码
    if datalist[0]==1:
        #print(datalist[1])
        token=datalist[1].strip('\"')
        ids=datalist[2]
        status=1
        return  status,ids,token
    else:
        status=0
        return status

#--------------------------------------------------------      
#case6--FSD添加tools
def test_FSD_add_tools():
    data=flyuser.testdata_FSD_login_userdata_001      
    toolsdata=flyuser.testdata_flyuser_add_tools_002
    ret=test_FSD_login(data)
    print(ret)   
    ids=ret[2]
    token=ret[1]
    toolsdata['memberId']=ids

    ids=str(ids)
    toolsdata['toolModel']="大疆 MG-1"
    ret=my_obj.add_fsd_tools(toolsdata,ids,token)
    
    if ret!=1:
        print('fail')
        
#--------------------------------------------------------        
#case7--fsd检查账号是否存在
def test_FSD_check_account(accountdata):
    #accountdata=flyuser.testdata_flyuser_add_tools_002
    my_obj = FSDLogin()
    
    ret=my_obj.fsd_check_account(accountdata)
    
    if ret!=0:
        print('account  is not exist')
    return ret
        
#--------------------------------------------------------  
def test_create_flyuser_team(ids,token,flyuserteamdata):

    datalist=my_obj.fsd_create_flyuser_team(ids,token,flyuserteamdata)
    print(datalist)
    if datalist!=1:
        print('Fail')
    
        
#--------------------------------------------------------  
def test_add_operate_car(ids,token,operatecardata):
    
    datalist=my_obj.fsd_add_operate_car(ids,token,operatecardata)
    #print(datalist)
    if datalist==1:
        print('Fail')

    return datalist            
#--------------------------------------------------------
def test_fly_auth(ids,token,phone,data):
    datalist=my_obj.fsd_fly_auth(ids,token,phone,data)
    if datalist!=1:
        print('Fail')
    return datalist



#--------------------------------------------------------        
def test_query_fly_auth(phone,queryauth):
    datalist=my_obj.query_fly_auth(phone,queryauth)
    print(datalist)
    if datalist[0]!=1:
        print('Fail')
    return datalist


#--------------------------------------------------------
def test_sys_flyuser_auth(ids,sysflyuserauth,headers):
    datalist=my_obj.sys_fly_user_auth(ids,sysflyuserauth,headers)
    print(datalist)
    if datalist!=1:
        print('Fail')
    return datalist


#--------------------------------------------------------
def test_sys_fly_auth(flyUserId,sysflyrauth,headers):
    datalist=my_obj.sys_fly_auth(flyUserId,sysflyrauth,headers)
    print(datalist)
    if datalist!=1:
        print('Fail') 

    return datalist


#--------------------------------------------------------
def test_fsd_add_plane(phone,userId,token,data):
    datalist=[]
    datalist=my_obj.fsd_add_plane(phone,userId,token,data)
    print(datalist)
    if datalist!=1:
        print('Fail')     
    return datalist

#--------------------------------------------------------
def test_get_plane_id(ids,token,phone):
    datalist=my_obj.fsd_get_plane_id(ids,token,phone)
    print(datalist)
    if datalist[0]!=1:
        print('Fail')     
    return datalist

#--------------------------------------------------------
def test_update_Xy(ids,token,phone):
    datalist=my_obj.fsd_update_Xy(ids,token,phone)
    print(datalist)
    if datalist!=1:
        print('Fail')  
    return datalist

#--------------------------------------------------------
def test_get_car_id(ids,token,phone):
    datalist=my_obj.fsd_get_car_id(ids,token,phone)
    print(datalist)
    if datalist[0]!=1:
        print('Fail')  
    return datalist

#--------------------------------------------------------
def test_get_reserve_calendar(ids,token,phone,carid):
    datalist=my_obj.fsd_get_reserve_calendar(ids,token,phone,carid)
    print(datalist)
    if datalist[0]!=1:
        print('Fail')
        
    return datalist


#--------------------------------------------------------
def test_query_crop_price(ids,token,phone,data,time):
    datalist=my_obj.query_crop_price(ids,token,phone,data,time)
    print(datalist)

    
    if datalist[0]!=1:
        print('Fail')

    else:
        maxprice=datalist[1]['maxPrice']
        minprice=datalist[1]['minPrice']
        print('maxprice:  ',maxprice)
        print('minprice:  ',minprice)
        
        

        return minprice,maxprice


#--------------------------------------------------------
def test_add_reserve_order(ids,token,phone,carid,planeid,price1,time1,data):
    
    datalist=my_obj.fsd_add_reserve_order(ids,token,phone,carid,planeid,price1,time1,data)
    print(datalist)
    if datalist[0]!=1:
        print('Fail')  

    return datalist


#--------------------------------------------------------        

    
if __name__ == "__main__" :
    
    #errorpassword=flyuser.testdata_FSD_login_password_error    
    #userdata=flyuser.testdata_FSD_login_userdata_001
    #check_account=flyuser.testdata_FSD_check_data_001


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


    #userid=2785
    #userid=ids   
    #test_sys_management_freez_flyuser(userid,farmtoken)
    #方法2
    #my_obj.sysment_management_nofreeze_flyuser(userid,farmtoken)


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
    

    

    
    
    
    

