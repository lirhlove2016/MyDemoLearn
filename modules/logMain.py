# -*- coding:utf-8 -*-

from common.logger import Logger

from conf import conf

from common.Log import MyLog as Log

#日志

#logger = Logger(logger="FSD TEST").getlog()

class LogMain():
    
    def __init__(self,title):
        self.flag=conf.logger_config
        print(self.flag)
        print(title)
        #self.logger = Logger(logger="FSD TEST").getlog()
        self.logger = Logger(logger=title).getlog()
        
 
    
    def run_info(self,message):
        """当为True时打印日志
        Usge:
        run_info('ceshi','message')

        """
        if self.flag:
            #logger = Logger(logger=title).getlog()
            self.logger.info(message)
        else:
            #
            pass
            

if __name__ == '__main__':

    mylogger = Logger(logger='--正在打印日志----').getlog()
    mylogger.info("这是一个日志文件")

    
    logger=LogMain("ceshi")
    logger.run_info('FSD login')


    log = Log.get_log()
    logger = log.get_logger()
    logger.info("test")
    logger.debug("test debug")
    logger.info("test info")



