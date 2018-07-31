# -*- coding:utf-8 -*-
# 批量用例执行--手工加载

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

#unittest
import unittest
from common import HTMLTestRunner
from  time  import sleep
#import HTMLTestRunner

#数据部分
my_obj = FSDLogin()
flyuserdata=flyuser.testdata_FSD_login_userdata_001
phone='14433334003'


class TestFSD_Login(unittest.TestCase):
    """fsd login"""
    
    def setUp(self):
        print('---------TEST START-------------')
        
    #case1--FSD用户登录 
    def test_fsd_login(self):
		
        datalist=[]
        #返回值
        datalist=my_obj.fsd_api_login(phone,flyuserdata)
        #print(datalist)
        
        if datalist[0]!=1:
            print('fail')
            return None
        else:
            #token=datalist[1]
            #userid=datalist[2]
            #print(token,userid)
            return datalist


    def tearDown(self):
        print('-------TEST END----------------- ')


if __name__ == '__main__':

    #unittest.main()

  
    # 1、构造用例集
    suite = unittest.TestSuite()

    # 2、执行顺序是安加载顺序：先执行test_sub，再执行test_add
    suite.addTest(TestFSD_Login("test_fsd_login"))
    #suite.addTest(TestOne("test_add"))

    # 3、实例化runner类
    runner = unittest.TextTestRunner()

    # 4、执行测试
    runner.run(suite)

