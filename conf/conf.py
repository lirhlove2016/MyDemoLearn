#!/usr/bin/env python
#_*_coding:UTF-8_*_

import os,time

#此处存放全局的参数，配置

#browser
browserName = "Firefox"
#browserName = "Chrome"
#browserName = "IE"


#logger
#logger_config=Flase   #关闭打印日志
logger_config=True  #开启logger日志打印


#设置report_path
report_dir="/results/report/"
report_path=os.path.abspath('.') + report_dir
#print(report_path)


log_dir='/results/logs/'
log_path=os.path.abspath('.')+log_dir       

#print(log_path)










