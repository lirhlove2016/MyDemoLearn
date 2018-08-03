#-*- coding: utf-8 -*-
'''
FSDLogin    
3.x
'''
__version__='0.1'

import string
import json
import sys
from common.basic_http import MyRequest
from conf import server_config as device
from conf import api_url as api
import time
import datetime
import random
import requests

from requests_toolbelt import MultipartEncoder


#2.7
#reload(sys) 
#sys.setdefaultencoding('utf8')


class FSDLogin(object):

    #------------FSD login Api-------------------------------------------
    def fsd_api_login(self,phone,flyuser_data):
        
        userdata=flyuser_data
        userdata['phone']=phone
        flyuser_login_url = api.API_URL['fsdlogin']
       
        print(userdata,'\n',flyuser_login_url)

        # 发送post请求
        my_request = MyRequest(flyuser_login_url,userdata)
        reslist=my_request.request_token_fsd()

        res=reslist[0]
        token=reslist[1]
        userId=reslist[2]
        
        #print('token=',token)
        #print('userId=',userId)

        res=res.json()
        print("response: ",res)
        

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        #print(ret)   

       #返回值不报错时
        if err_flag==True:
            print('FSD login successed')          
            flag_fsd_login_status=1
            return flag_fsd_login_status,token,userId
                      
        elif '密码不正确' in ret:            
            print('FSD login error password',ret)
            flag_fsd_login_status = 2
            return flag_fsd_login_status
        elif '账户已冻结' in ret:
            print('Freeze fly account can not login',ret)
            flag_fsd_login_status = 3
            return flag_fsd_login_status
        else:
            print('Failed:FSD login failed')
            flag_fsd_login_status = 0
            return flag_fsd_login_status    

        
    #------------System Management login ------------------------------------------
    def system_management_login(self,sys_data):
        userdata=sys_data
        request_url = api.API_URL['syslogin']
        
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)

        reslist=my_request.request_token_sys()
        res=reslist[0]
        farmtoken=reslist[1]
        
        print('farmtoken=',farmtoken)
        
        res=res.json()
        print("response ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        print(ret)
        
        #返回值不报错时
        if err_flag==True:  

            #登录成功，返回登录状态flag,token
            print('passed:System login successed')
            flag_sys_login_status=1
            return flag_sys_login_status,farmtoken
        else:
            print('Failed:System login failed')
            flag_sys_login_status = 0
            return flag_sys_login_status    


    #------------System Management Freeze flyuser ------------------------------------------
    def sysment_management_freeze_flyuser(self,userid,token):
        #只传入userid

        userdata={}
        userdata["id"]=userid
        userdata["state"]=3
        headers={}
        headers['FARMFRIEND_TOKEN']=token
        
        request_url = api.API_URL['freezeflyaccount']

        print(userdata,'\n',request_url,headers)
        # 发送post请求
        my_request = MyRequest(request_url,userdata,headers)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)
        #转换成Str
        jsonres=json.dumps(res)

        # 解析response返回信息

        if 'SUCCESS' in jsonres:
            print('Passed: freeze fly account successed')
            flag_freez_ret = 1
            return flag_freez_ret
        else:
            print('Failed:freeze fly account failed')
            flag_freez_ret = 0
            return flag_freez_ret


    #------------System Management not Freeze flyuser ------------------------------------------
    def sysment_management_nofreeze_flyuser(self,userid,token):
        #只传入userid

        userdata={}
        userdata["id"]=userid
        userdata["state"]=2

        heads={}
        heads['FARMFRIEND_TOKEN']=token
        
        request_url = api.API_URL['freezeflyaccount']
        print(userdata,'\n',request_url)
        # 发送post请求
        my_request = MyRequest(request_url,userdata,heads)
        res = my_request.request_token_post(token)
        
        res=res.json()
        print("response: ",res)

        jsonres=json.dumps(res)
        # 解析response返回信息
        if 'SUCCESS' in jsonres:
            print('Passed: no freeze fly account successed')
            flag_freez_ret = 1
            return flag_freez_ret
        else:
            print('Failed:no freeze fly account failed')
            flag_freez_ret = 0
            return flag_freez_ret
   

    #------------FSD Register api ------------------------------------------
    def fsd_api_register(self,phone):
        userdata={}
        request_url = api.API_URL['fsdregister']
        
        print('Test data and api url |',userdata,'| ',request_url)
        
        userdata['phone']=phone
        # 发送post请求
        my_request = MyRequest(request_url,userdata)

        reslist=my_request.request_token_fsd()

        res=reslist[0]
        token=reslist[1]
        userId=reslist[2]
        
        print('token=',token)
        print('userId=',userId)

        res=res.json()
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        #print(ret)

        #返回值不报错时
        if err_flag==True:

            print('FSD register successed')          
            flag_status=1
            return flag_status,token,userId
                      
        else:
            print('FSD register failed')
            flag_fsd_login_status = 0
            return flag_fsd_login_status                

    
    #------------FSD set password  ------------------------------------------
    def flyuser_set_password(self,accesstoken,ids,phone,password):
        userdata={}
        userdata['userId']=ids
        userdata['password']=password
        userdata['phone']=phone
        userdata['token']=accesstoken
        
        request_url = api.API_URL['fsdusersetpassword']
       
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)
        

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if res['info']=='操作成功':
            print('Passed: flyuser set password successed')
            flag_fsd_setpassword = 1
            return flag_fsd_setpassword
        else:
            print('Failed:flyuser set password failed')
            flag_fsd_setpassword = 0
            return flag_fsd_setpassword


    #------------random phone number ------------------------------------------
    def ramdom_phone_number(self):

        # 配置FSD信息
        num_start = ['142','143','141','144','140']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits,8))
        res = start+end
        return res


    #------------FSD add tools ------------------------------------------
    def add_fsd_tools(self,data,ids,token):
        userdata=data
        userdata['id']=ids
        userdata['TOKEN']=token
        
        request_url = api.API_URL['addtools'].replace("id",ids).replace("TOKEN",token)
        
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #jsonres=json.dumps(res)
        if res['info']=='操作成功':

            print('Passed: flyuser add tools successed. ')
            flag_fsd_add_tools = 1
            return flag_fsd_add_tools
        else:
            print('Failed: flyuser add tools failed')
            flag_fsd_add_tools = 0
            return flag_fsd_add_tools


    #------------FSD check account api  ------------------------------------------
    def fsd_check_account(self,check_userdata):

        userdata=check_userdata
        request_url = api.API_URL['fsdcheckaccount']
        
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)
        
        
        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        #将字典转换成字符
        ret=json.dumps(ret)
        if 'user not exist' in ret:
            print(' flyuser account not exist')
            flag_fsd = 1 
        
        else:
            print('flyuser account  exist')
            flag_fsd = 0
 
        return flag_fsd

    #------------FSD create flyuser team api ------------------------------------------
    def fsd_create_flyuser_team(self,ids,token,flyuserteamdata):

        userdata=flyuserteamdata       
        print(userdata)
        ids=str(ids)
        request_url = api.API_URL['createflyuserteam'].replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        if res['info']=='操作成功':
            print('Passed: FSD create flyuser team successed. ')
            flag_fsd = 1

        elif "已经创建团队的老板不能再创建团队" in res['info']:
            flag_fsd=2
            print('Failed: 已经创建团队的老板不能再创建团队. ')
        else:
            print('Failed: FSD create flyuser team  failed')
            flag_fsd = 0

        return flag_fsd

        
     #------------FSD add operate car api ------------------------------------------
    def fsd_add_operate_car(self,ids,token,data):
        userdata=data
        userdata['memberId']=ids
  
        ids=str(ids)
      
        request_url = api.API_URL['addoperatecar'].replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if ret==1:
            print('Passed: add operate car successed. ')
            flag_fsd = 1
        else:
            print('Failed: add operate car  failed')
            flag_fsd = 0

        return flag_fsd


    #------------FSD add plane api ------------------------------------------
    def fsd_add_plane(self,phone,ids,token,data):
        userdata=data
        userdata['memberId']=ids
        userdata['phone']=phone
          
        ids=str(ids)
        phone=str(phone)
        print(phone)
      
        request_url = api.API_URL['addplane'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if res['info']=='操作成功':
            print('Passed: add plane successed. ')
            flag_fsd = 1
        else:
            print('Failed: add plane  failed')
            flag_fsd = 0

        return flag_fsd


    
     #------------FSD get plane id------------------------------------------
    def fsd_get_plane_id(self,ids,token,phone):
        userdata={}
        userdata['memberId']=ids
        userdata['from']='3'
        userdata['reserveId']=''
          
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['getplaneid'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if '操作成功' in res['info']:
            print('Passed: fsd get plane id successed. ')
            planeid=res['datas']["toolList"][0]['toolId']
            print('Get the planeid %s'%planeid)
            flag_fsd = 1
            return flag_fsd,planeid
        else:
            print('Failed: fsd get plane id  failed')
            flag_fsd = 0
            return flag_fsd


    
     #------------FSD update  Xy------------------------------------------
    def fsd_update_Xy(self,ids,token,phone):
        userdata={}
        x="116.483189"
        y="39.997527"
          
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['updatexy'].replace("XVALUE",x).replace("YVALUE",y).replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if '操作成功' in res['info']:
            print('Passed: update xy successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed: update xy failed')
            flag_fsd = 0
            return flag_fsd

     #------------FSD get car id------------------------------------------
    def fsd_get_car_id(self,ids,token,phone):
        userdata={}
          
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['getcarid'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed: fsd get car id successed. ')
            carid=res['data']['list'][0]['id']
            print('Get the car id %s'%carid)
            flag_fsd = 1
            return flag_fsd,carid
        else:
            print('Failed: fsd get car id  failed')
            flag_fsd = 0
            return flag_fsd

     #------------FSD get reserve calendar------------------------------------------
    def fsd_get_reserve_calendar(self,ids,token,phone,carid):
        userdata=int(carid)
        print(type(carid))
              
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['getreservecalendar'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed: get reserve calendar successed. ')
            times=res['data'][0]['time']
            print('Get the times %s'%times)
            flag_fsd = 1
            return flag_fsd,times
        else:
            print('Failed: get reserve calendar  failed')
            flag_fsd = 0
            return flag_fsd

        
     #------------FSD get reserve calendar------------------------------------------
    def query_crop_price(self,ids,token,phone,time):

        regions={"province":"北京市","provinceCode":110000,"city":"北京市","cityCode":110100}

        userdata={}
        userdata['times']=1525478400
        userdata['regions']=regions
        print(userdata)
                 
        ids=str(ids)
        phone=str(phone)

      
        request_url = api.API_URL['querycropprice'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed: query crop price successed. ')
            maxPrice=res['data'][0]['maxPrice']
            scmaxPrice= res['data'][0]['scMaxPrice']          
            minPrice=res['data'][0]['minPric']  
            exceed=res['data'][0]['exceedScale']
            print('Get the maxPrice %s'%maxPrice)
            print('Get the scmaxPrice %s'%scmaxPrice)
            print('Get the minPrice %s'%minPrice)
            print('Get the exceed %s'%exceed)

            adviceprice=res['data'][0]['advicePrice']
            inputprice= res['data'][0]['inputPrice']          
            cropname=res['data'][0]['cropName']
            cropid=res['data'][0]['cropId']
            print('Get the adviceprice %s'%adviceprice)
            print('Get the inputprice %s'%inputprice)
            print('Get the minPrice %s'%cropname)
            print('Get the exceed %s'%cropid)

            data=res['data']
            retuendata={}
            returndata['maxPrice']=maxPrice
            returndata['scmaxPrice']=scmaxPrice
            returndata['minPrice']=minPrice
            returndata['exceed']=exceed
            returndata['adviceprice']=adviceprice
            returndata['inputprice']=inputprice
            returndata['cropname']=cropname
            returndata['cropid']=cropid            
            
            flag_fsd = 1
            return flag_fsd,returndata
        else:
            print('Failed: query crop price  failed')
            flag_fsd = 0
            return flag_fsd



     #------------FSD add reserve order------------------------------------------
    def fsd_add_reserve_order(self,ids,token,phone,carid,planeid,price,time):
        userdata={}

        regions={"province":"北京市","provinceCode":110000,"city":"北京市","cityCode":110100}

        regionPrices=[{"cropId":2,"province":"北京市","city":"市辖区","provinceCode":110000,"cityCode":110100,"minPrice":4,"cropName":"中稻","scMaxPrice":0,"exceedScale":90,"maxPrice":12.0,"advicePrice":"","inputPrice":4.5}]

        regionPrices[0]['inputPrice']=price
              
        userdata['userId']=ids
        userdata['carId']=carid
        userdata['planes']='[2102]'
        userdata['regions']=regions
        userdata['regionPrices']=regionPrices
        userdata['times']=time
        
             
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['addreserveorder'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed:add reserve order successed. ')
            orderid=res['data']
            print('Get the orderid %s'%orderid)
            flag_fsd = 1
            return flag_fsd,orderid
        else:
            print('Failed: add reserve order  failed')
            flag_fsd = 0
            return flag_fsd


     #------------query fly user auth ------------------------------------------
    def query_fly_auth(self,phone,userdata):

        userdata['phone']=phone
        request_url = api.API_URL['queryflyuser']
                
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_management(res)     
        print(ret)

        if err_flag==True:

            print('Passed:query flyuser successed.')          
            flag_status=1
            id=res['data']['data'][0]['id']
            return flag_status,id
                      
        else:
            print('Failed:query flyuser failed')
            flag_status = 0
            return flag_status  

     #------------ sys fly user auth 实名认证------------------------------------------
    def sys_fly_user_auth(self,id,userdata):

        userdata['id']=id
        request_url = api.API_URL['sysflyuserauth']
               
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if "SUCCESS" in res['info']:
            print('Passed:sys flyuser auth successed.')          
            flag_status=1
            return flag_status
        elif "此飞手已审核" in res['info']:
            print('Failed :sys flyuser auth failed.')          
            flag_status=2
            return flag_status
        else:
            print('Failed:sys flyuser auth failed.')
            flag_status = 0
            return flag_status  

     #------------ sys fly user auth 飞手认证------------------------------------------
    def sys_fly_auth(self,flyUserId,userdata):

        userdata['flyUserId']=id
        request_url = api.API_URL['sysflyauth']
               
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if err_flag==True:
            if "SUCCESS" in res:
                print('Passed:sys fly auth successed.')          
                flag_status=1
                return flag_status
           
            print('Passed:sys fly auth successed.')          
            flag_status=1
            return flag_status

        elif  "此飞手已审核" in res['info']:
                print('Failed :sys fly auth failed.')          
                flag_status=2
                return flag_status              
        else:
            print('Failed:sys fly auth failed')
            flag_status = 0
            return flag_status
        
    
#new			
# ----------------------------------------------------------------------------------------
    def sys_queryorderlist(self,token,orderNumber):
        '''
            management queryorder  查看订单。

            参数:

            举例:
            | management queryorder |
        '''
        # 配置信息
        userdata={
            "0":"p",
            "1":"o",
            "2":"s",
            "3":"t",
            "isTest":"0",
            "type":"1",
            "makePeople":"",
            "acceptOrderPeople":"",
            "phone":"",
            "salesman_name":"",
            "order_number":"",
            "crops_name":"-1",
            "isPay":"-1",
            "state":"-1",
            "flyUserType":"-1",
            "medicineServie":"-1",
            "teamWork":"-1",
            "hasMedicine":"-1",
            "isLongReserve":"-1",
            "sopTagid":"",
            "startCreateTime":"2018-01-01",
            "endCreateTime":"2018-12-31",
            "region":"",
            "sonCompanyId":"-1",
            "salesmanId":"-1",
            "workAddress":"",
            "fromSalesmanManage":"0",
            "page":"1",
            "sort":"30",
            "sort":"",
            "order":"",
            }
        headers={}
        headers["Content-Type"]="application/x-www-form-urlencoded"
        headers["FARMFRIEND_TOKEN"]=token
        
        url_string = api.API_SYS_URL['queryflyorderlist']

        # 发送request到NTGJAPI
        my_request = MyRequest(url_string,userdata,headers)
        res = my_request.request_post()
        res=res.json()
        #print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
	
		
        # 解析response返回信息

        if 'SUCCESS' in res['info']:
            print('Passed:sys query orderlist  successed')
            order_id=res['datas']['data'][0]['id']
            print('get order_id of %s'%(order_id))

            flag_status=1
            return flag_status,order_id
        else:
            print('Failed:sys query orderlist failed')
            flag_status=0
            return flag_status

    # ----------------------------------------------------------------------------------------	
    def sys_queryassignflyuser(self,token,order_id,phonenumber,data):

        userdata={}
        userdata=data
        userdata['id']=order_id
        userdata['phone']=phonenumber
        
        today=datetime.date.today()
        userdata['time']=today
        headers={}
        headers["Content-Type"]="application/x-www-form-urlencoded"
        headers["FARMFRIEND_TOKEN"]=token
        
        url_string = api.API_SYS_URL['queryflyuser']

        print('Test data and api url |',userdata,'| ',url_string)

        # 发送request到NTGJAPI
        my_request = MyRequest(url_string,userdata,headers)
        res = my_request.request_post()
        res=res.json()
        #print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
	
		
        # 解析response返回信息

        if 'data' in res:
            print('Passed:sys query assign flyuser  successed')
            flyuser_id=res['data']['data'][0]['id']
            print('get flyuser_id of %s'%(flyuser_id))

            flag_status=1
            return flag_status,flyuser_id
        else:
            print('Failed:sys query assign flyuser failed')
            flag_status=0
            return flag_status

    # ----------------------------------------------------------------------------------------	
    def sys_publishorder(self,token,order_id,order_number,flyuser_id,data):

       

        userdata={}
        userdata=data
        userdata['id']=order_id
        userdata['orderNumber']=order_number
        userdata['flyUser']=flyuser_id
        today=datetime.date.today()
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d')
        userdata['workStartTime']=nowTime
        
        headers={}
        headers["Content-Type"]="application/x-www-form-urlencoded"
        headers["FARMFRIEND_TOKEN"]=token
        
        url_string = api.API_SYS_URL['publishorder']

        # 发送request到NTGJAPI
        my_request = MyRequest(url_string,userdata,headers)
        res = my_request.request_post()
        res=res.json()
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
	
		
        # 解析response返回信息
        
        if err_flag:
            print('Passed:sys  publishorder  successed')
      
            flag_status=1
            return flag_status
        else:
            print('Failed:sys  publishorder failed')
            flag_status=0
            return flag_status

    #------------FSD msgcenter-----------------------------------------
    def fsd_msg_center(self,ids,token,data):
        userdata={}
        userdata=data
        ids=str(ids)
        userdata['outer_uid']=ids
      
        request_url = api.API_URL['msgcenter'].replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        #print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  res['errno']==0:
            print('Passed: fsd msgcenter successed. ')
            msgid=res['data'][0]['id']
            print('Get the msg id %s'%msgid)

            text=res['data'][0]['text']
          
            flag_fsd = 1
            return flag_fsd,msgid,text
        else:
            print('Failed: fsd msgcenter failed')
            flag_fsd = 0
            return flag_fsd        

    #------------FSD msgcenter-----------------------------------------
    def fsd_orderpromtquery(self,ids,token,phone,msgid,ordernumber):
        userdata={}
        userdata['msgId']=msgid
        userdata['orderNumber']=ordernumber
        
        phone=str(phone)
        ids=str(ids)
        request_url = api.API_URL['orderPromptQuery'].replace("id",ids).replace("TOKEN",token).replace("PHONE",phone)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  '操作成功' in res['info']:
            print('Passed: fsd orderPromptQuery successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed:fsd orderPromptQuery failed')
            flag_fsd = 0
            return flag_fsd

    #------------FSD updateorderstate----------------------------------------
    def fsd_updateorderstate(self,ids,token,phone,msg_id,ordernumber,data,order_text):
        userdata={}
        userdata=data
        userdata['state']=3  
        userdata['userid']=ids       
        userdata['orderNumber']=ordernumber
        userdata['order_amount']=order_text['total_money']
        userdata['work_time']=order_text['work_time']
        userdata['msgId']=msg_id
                
        phone=str(phone)
        ids=str(ids)
        request_url = api.API_URL['updateorderstate'].replace("id",ids).replace("TOKEN",token).replace("PHONE",phone)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  res['errorCode']==0:
            print('Passed: fsd updateorderstate successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed:fsd updateorderstate failed')
            flag_fsd = 0
            return flag_fsd

    

    

    #------------FSD updateorderstate----------------------------------------提交作业报告
    def fsd_submitorder(self,ids,token,phone,msg_id,ordernumber,data,area):
        userdata={}
        userdata=data
        userdata['userid']=ids       
        userdata['orderNumber']=ordernumber
        userdata['actual_area']=area
        userdata['fly_actual_area']=area
        userdata['msgId']=msg_id

        querystring ={"access_phone":"18301212965","userId":"2187","token":"bddd03f4a404463690a7fd6013d722f4"}

        json_data = "state=4&userid="+str(ids)+"&orderNumber="+str(ordernumber)+"&fly_actual_area="+str(area)+"&actual_area="+str(area)+"&msgId="+str(msg_id)+"&totalSprayedDays=1&actualWorkStartTime=1532964060&actualWorkEndTime=1533050460&serviceConfirmSheet=%5B%22http%3A%5C%2F%5C%2Ffarmlandbucketstest.oss-cn-beijing.aliyuncs.com%5C%2F07b6fd8d8aaf4008814e31a3894efc92%22%5D&medicalInformation=%5B%7B%22drugNumber%22%3A0.0%2C%22drugPositiveUrl%22%3A%22http%3A%2F%2Ffarmlandbucketstest.oss-cn-beijing.aliyuncs.com%2Fd6a45d9bdb9843f88fa865ef402c2182%22%2C%22drugReverseUrl%22%3A%22%22%2C%22unitMu%22%3A0.0%7D%5D"

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            }

        phone=str(phone)
        ids=str(ids)
        request_url = api.API_URL['updateorderreport'].replace("id",ids).replace("TOKEN",token).replace("PHONE",phone)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求        
        my_request = MyRequest(request_url,userdata,headers)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  '操作成功' in res['info'] or res['errorCode']==0:
            print('Passed: fsd submitorder successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed:fsd submitorder failed')
            flag_fsd = 0
            return flag_fsd


    #------------FSD orderboundquery----------------------------------------
    def fsd_orderbundquery(self,ids,token,phone,ordernumber):
        userdata={}     
        userdata['orderNumber']=ordernumber
        userdata['taskOrderType']=1

                
        phone=str(phone)
        ids=str(ids)
        request_url = api.API_URL['orderBoundQuery'].replace("id",ids).replace("TOKEN",token).replace("PHONE",phone)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  res['errno']==0 or res['errno']!=13:
            print('Passed: fsd orderboundquery successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed:fsd orderboundquery failed')
            flag_fsd = 0
            return flag_fsd

    #------------FSD getteammanageinfo----------------------------------------
    def fsd_get_team_info(self,ids,token,phone,ordernumber):
        userdata={}     
        userdata['orderNumber']=ordernumber
                
        phone=str(phone)
        ids=str(ids)
        request_url = api.API_URL['getteaminfo'].replace("id",ids).replace("TOKEN",token).replace("PHONE",phone)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  res['errorCode']==0 or res['errno']!=13:
            print('Passed: fsd getTeaminfo successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed:fsd getTeaminfo failed')
            flag_fsd = 0
            return flag_fsd



#------------YWB login----------------------------------------
    def ywb_login(self,data):
        userdata={}
        userdata=data       

        request_url = api.API_YWB_URL['ywblogin']
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  res['errorCode']==0 or res['errno']!=13:
            accountId=res['datas']["loginSuccess"]["accountId"]
            token=res['datas']["loginSuccess"]["token"]

            print('Get the token is %s'%token)
            print('Get the accountId is %s'%accountId)
            
            print('Passed: ywb login successed. ')
            flag_ywb = 1
            return flag_ywb,accountId,token
        else:
            print('Failed:ywb login failed')
            flag_ywb = 0
            return flag_ywb


#------------YWB salemanquery----------------------------------------
    def ywb_salesmanquery(self,ids,token,data,phone):
        userdata={}
        userdata=data       
        
        phone=str(phone)
        ids=str(ids)
        request_url = api.API_YWB_URL['salesmanquery'].replace("id",ids).replace("TOKEN",token).replace("PHONE",phone)
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)


        if  res['errorCode']==0 or res['errno']!=13:
            
            print('Passed: ywb salesmanquery successed. ')
            flag_ywb = 1
            return flag_ywb
        else:
            print('Failed:ywb salesmanquery failed')
            flag_ywb = 0
            return flag_ywb

#------------YWB add order----------------------------------------
    def ywb_addorder(self,ids,token,phone,values):
        userdata={}
        userdata=values
        datas= MultipartEncoder(fields={'data': str(json.dumps(values))}) 

        headers = {
            "content-type": datas.content_type
        }

               
        phone=str(phone)
        ids=str(ids)
        request_url = api.API_YWB_URL['addorder'].replace("id",ids).replace("TOKEN",token).replace("PHONE",phone)

      
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,datas,headers)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)


        if  res['errorCode']==0 or res['errorCode']!=13:
            order_number=res['datas']["payment"]["order_number"]

            print('Get the ordernumber is %s'%order_number)
            
            print('Passed: ywb addorder successed. ')
            flag_ywb = 1
            return flag_ywb,order_number
        else:
            print('Failed:ywb addorder failed')
            flag_ywb= 0
            return flag_ywb



#------------MenDian ----------------------------------------
    def mendian_getwxuserinfo(self,data):
        userdata={}
        userdata=data       

        request_url = api.API_MD_URL['getwxuserinfo']
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  res['errno']==0 or res['errno']!=13:

            token=res['data']["token"]
            userid=res['data']["accountId"]
            print('Get the MD token is %s'%token)
            print('Get the MD userid is %s'%userid)
            
            print('Passed: mendian getuserinfo  successed. ')
            flag_md = 1
            return flag_md,token,userid
        else:
            print('Failed:mendian getuserinfo failed')
            flag_md= 0
            return flag_md

#------------MenDian ----------------------------------------
    def mendian_addorder(self,token,userid,data):
        userdata={}
        userdata=data       

        request_url = api.API_MD_URL['wxaddorder']
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if  res['errno']==0 or res['errno']!=13:

            prepayid=res['data']["prePayId"]
            groupmembercount=res['data']["groupMemberCount"]
            preferentialList=res['data']['preferentialList']
            print('Get the prepayid is %s'%prepayid)
            print('Get the groupMemberCount is %s'%groupmembercount)
            
            print('Get the  preferentialList is %s'% preferentialList)
            
            print('Passed: mendian addorder  successed. ')
            flag_md = 1
            return flag_md,prepayid,groupmembercount, preferentialList
        else:
            print('Failed:mendian addorder failed')
            flag_md= 0
            return flag_md




        
#-----------------------------------------
        
if __name__ == "__main__" :

    my_obj = FSDLogin()
    '''
    data2= {
            'phone':'19900001001',
            "password":"123qwe",
    }
    my_obj.fsd_api_login(data2)
 
    data3 = {
        "userName":"lirunhua",
        "passWord":"12345",
    }
    #my_obj.system_management_login(data3)
    data4 = {
        "id":'2803',
        "state":'3',
    }
    my_obj.sysment_management_freeze_flyuser(data4)
    '''

    item="\"FARMFRIEND_TOKEN\":"
    res={'errno': 0, 'data': {'FARMFRIEND_TOKEN': 'eyJ1aWQiOiI3NSIsInRva2VuIjoiYTNjNTJhYzEtYjVkMS00Yjc3LTk5MTQtMDZhZjNkYzM2N2ZlIn0=', 'FARMFRIEND_LT': '1524507681800'}}
    

