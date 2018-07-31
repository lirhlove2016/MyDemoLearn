#-*- coding: utf-8 -*-
'''
封装get,post

'''
__version__='0.1'

import json
import requests
from conf import server_config as device
from conf import api_url as api
import pymysql

#  ----------------------------------------------------发送Json配置到Api


class MyRequest(object):
    myresponse = ''
    

    def __init__(self,url,dict_data,header={}):
        
        self.host_ip = device.DICT__NTGJ_HTTP_SERVER['IP']
        self.port = device.DICT__NTGJ_HTTP_SERVER['HTTP_PORT']        
        self.timeout = device.TIMEOUT_10s
        self.headers = header		
        self.data = dict_data
        self.url = url
        self.auth_token = None
  
        self.url = url

		
			
        
    #-------------------defined http get method------------------------------------------------
    def request_get(self):
        """
        defined get method
        :return:
        """
        print('------------------------------------------------------------------------------')
        print('start get request....')
              
        print("ip:",self.host_ip)
        print('port:',self.port)
        print('url:',self.url)
        print('timeout:',self.timeout)
        try:
            response = requests.get('http://'+self.host_ip+ ":" + self.port + self.url, params=self.data,headers=self.headers,timeout=float(self.timeout))
            return response
        except TimeoutError:
            print(" %S Time out!" %self.url)
            return None

    #--------------------defined http post method------------------------------------------------
    def request_post(self):
        """
        defined post method
        :return:
        """
        print('------------------------------------------------------------------------------')
        print('start post request....')
        
        print("ip:",self.host_ip)
        print('port:',self.port)
        print('url:',self.url)
        print('timeout',self.timeout)

        if self.headers=={}:
            self.headers=device.DICT__Register_HEADERS
		
        print(self.headers)
        print('post data ',self.data)
        try:
            response = requests.request('POST','http://'+self.host_ip+ ":" + self.port + self.url,data=self.data,headers=self.headers,timeout=float(self.timeout))
            #print('response.text',response.text)

            return response
    
        except TimeoutError:
            print(" %S Time out!" %self.url)
            return None



    #--------------------get_cookies------------------------------------------------
    def get_cookies(self,response):
            #
            print(type(response.cookies))
            for k,v in response.cookies.items():
                print(k+':'+v)

            #获取cookies
            print('response.cookies',response.cookies)

   #--------------------decode_errorinfo_------------------------------------------------

    #总
    def decode_res_info(self,ret):
        '''
            返回：response中的 error_no 和 error_string 信息。           
        '''   
        response_json_dict=ret
  
        if 'errorCode' in response_json_dict:         
            error_no = response_json_dict['errorCode']
        elif 'errno' in response_json_dict:           
            error_no = response_json_dict['errno']
        elif 'resCode' in response_json_dict:
            error_no=response_json_dict['resCode']   
        
        print('errorno = %s'%(error_no))
        
        #error_no!=0 时的errmsg
        if error_no!=0 and error_no!=13 :
            error_msg=  response_json_dict['info']
            print ('error_msg = %s'%(error_msg))
        
        elif  error_no==13:
            error_msg=  response_json_dict['errmsg']
            print ('error_msg = %s'%(error_msg))
        elif error_no==1:
            error_msg=response_json_dict['info']  

        #print ('error_msg = %s'%(error_msg))
            

        #不报错时，返回数据信息
        if error_no==0: 
            ret_value = ''
            error_flag=True
            if 'data' in response_json_dict:
                ret_value = response_json_dict['data']
            elif 'body' in response_json_dict:
                ret_value = response_json_dict['body']
            
            elif 'resCode' in response_json_dict:
                error_no=response_json_dict['resCode']

            elif 'info' in response_json_dict:
                ret_value = response_json_dict['info']

            else:
                ret_value = ''  
            
            #print('decode_response_value',ret_value)            
            return error_flag,ret_value
        elif error_no==13:
            error_flag=True
            return error_flag,error_msg
        else:
            error_flag=False
            return error_flag,error_msg         




    #--------------------decode_errorinfo_from_management------------------------------------------------

    #管理后台的返回
    def decode_errorinfo_from_management(self,ret):
        '''
            返回：response中的 error_no 和 error_string 信息。           
        '''   
        response_json_dict=ret
  
        if 'errorCode' in response_json_dict:         
            error_no = response_json_dict['errorCode']
        elif 'errno' in response_json_dict:           
            error_no = response_json_dict['errno']
        elif 'resCode' in response_json_dict:
            error_no=response_json_dict['resCode']   
        print('errorCode = %s'%(error_no))
        
        #error_no!=0 时的errmsg
        if error_no!=0 and error_no!=13 :
            error_msg=  response_json_dict['info']
            print ('error_msg = %s'%(error_msg))

        elif  error_no==13:
            error_msg=  response_json_dict['errmsg']
            print ('error_msg = %s'%(error_msg))
            
        #print ('error_msg = %s'%(error_msg))
            

        #不报错时，返回数据信息
        if error_no==0:  
            ret_value = ''
            error_flag=True
            if 'data' in response_json_dict:
                ret_value = response_json_dict['data']
            elif 'body' in response_json_dict:
                ret_value = response_json_dict['body']
            
            elif 'resCode' in response_json_dict:
                error_no=response_json_dict['resCode']

            elif 'info' in response_json_dict:
                ret_value = response_json_dict['info']

            else:
                ret_value = ''  
            
            #print('decode_response_value',ret_value)            
            return error_flag,ret_value

        else:
            error_flag=False
            return error_flag,error_msg			

    #--------------------decode_errorinfo_from_FSD------------------------------------------------
    #飞手端的返回
    def decode_errorinfo_from_FSD(self,ret):
        '''
            返回：response中的 error_no 和 error_string 信息。           
        '''     
        response_json_dict=ret

        if 'errorCode' in response_json_dict:         
            error_no = response_json_dict['errorCode']
        elif 'errno' in response_json_dict:           
            error_no = response_json_dict['errno']
        elif 'resCode' in response_json_dict:
            error_no=response_json_dict['resCode']
   
        print('errorCode = %s'%(error_no))
        
        #error_no!=0 时的errmsg
        if error_no!=0 and error_no!=13 :
            error_msg=  response_json_dict['info']
            print ('error_msg = %s'%(error_msg))
        
        elif  error_no==13:
            error_msg=  response_json_dict['errmsg']
            print ('error_msg = %s'%(error_msg))  

        
        #不报错时，返回数据信息
        if error_no==0:  
            ret_value = ''
            error_flag=True
            if 'datas' in response_json_dict:
                ret_value = response_json_dict['datas']

            elif 'body' in response_json_dict:
                ret_value = response_json_dict['body']

            elif 'data' in response_json_dict:
                ret_value = response_json_dict['data']
            elif 'info' in response_json_dict:
                ret_value = response_json_dict['info']

            else:
                ret_value = ''              
            #print('decode_response_value',ret_value)
           
            return error_flag,ret_value 

        elif error_no==13:
            error_flag=False
            return error_flag,error_msg

        else:
            
            error_flag=False
            return error_flag,error_msg

        
    #--------------------sys login take farmtoken---------------------------------------------
    def request_token_sys(self):

        print('------------------------------------------------------------------------------')
        print('start post request....')
        
        print("ip:",self.host_ip)
        print('port:',self.port)
        print('url:',self.url)
        print('timeout',self.timeout)

 
        #data_json={"errno":0,"data":{"FARMFRIEND_TOKEN":"eyJ1aWQiOiI3NSIsInRva2VuIjoiNTI0M2FkNjctZGNlMi00YmUxLTgzNmYtYjk2MjA3NjljNzc3In0=","FARMFRIEND_LT":"1524534270484"}}
        headers={}
        headers['Content-Type']='application/x-www-form-urlencoded'
        print()
        print('post data',self.data)
        
        syslogin_url='http://'+self.host_ip+ ":" + self.port + self.url
        try:
            response = requests.post(syslogin_url,data=self.data,headers=headers,timeout=float(self.timeout))

            r=response.json()
            print('text',response.text)
            #print('json',r,type(r))

            farmtoken=r["data"]["FARMFRIEND_TOKEN"]
            print(farmtoken)
            return response,farmtoken

        except TimeoutError:
                print(" %S Time out!" %self.url)
                return None
        

     #--------------------fsd login take token------------------------------------------------
    def request_token_fsd(self):
        print('------------------------------------------------------------------------------')
        print('start post request....')        
        print("ip:",self.host_ip)
        print('port:',self.port)
        print('url:',self.url)
        print('timeout',self.timeout)
                                 
        headers={}
        headers['Content-Type']='application/x-www-form-urlencoded'
        headers['User-Agent']='Mozilla/4.0'

        print(headers)
        print('post data ',self.data)
        
        fsdlogin_url='http://'+self.host_ip+ ":" + self.port + self.url
        try:
            response = requests.post(fsdlogin_url,data=self.data,headers=headers,timeout=float(self.timeout))
            #response = requests.post(url3,data=data,headers=headers)

            t=response.text
            r=response.json()
            #print('response',response.text)
            
            token=r["datas"]['loginSuccess']["token"]
            userId=r["datas"]['loginSuccess']["userId"]
            #print(token)
            return response,token,userId

        except TimeoutError:
            print(" %S Time out!" %self.url)
            return None


    #-------------------- defined http post method--------------------------------------------
    def request_token_post(self,token):
        """
        defined post method
        :return:
        """
        print('------------------------------------------------------------------------------')
        print('start post request....')
        
        print("ip:",self.host_ip)
        print('port:',self.port)
        print('url:',self.url)
        print('timeout',self.timeout)
        
        headers=device.DICT__SYS_HEADERS
        headers['FARMFRIEND_TOKEN']=token
        print(headers)
        self.headers=headers
        print(self.headers)
        try:
            response = requests.post('http://'+self.host_ip+ ":" + self.port + self.url, params=self.data,headers=self.headers,timeout=float(self.timeout))
            #print('response.text',response.text)

            return response
    
        except TimeoutError:
            print(" %S Time out!" %self.url)
            return None
			
			
if __name__ == "__main__":

    print("start request")
    url='/management/sys/login'
    data = {
    "userName":"lirunhua",
    "passWord":"123456",
    }
    my_obj = MyRequest(url,data)
    my_response = my_obj.request_post()
    print('response.text',my_response.text)

    print('response.json()',my_response.json())

    print('response.content',my_response.content)

    print(type(my_response))
    
    my_obj.decode_errorinfo_from_management(my_response.json())

    #flyuser_login
    login_url='/flyHandApp/api/user/loginPassword'
    data2= {
            'phone':'19900001001',
            "password":"123qw",
    }

    
    my_obj = MyRequest(login_url,data2)
    my_response = my_obj.request_post()
    print('response.json()',my_response.json())

    f,v=my_obj.decode_errorinfo_from_FSD(my_response.json())
    if f:
        print(v)
    elif "密码不正确" in v:
            print('密码不正确')
        

 




    
