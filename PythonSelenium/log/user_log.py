#coding = utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        #self.logger.setLevel(logging.DEBUG)

        '''
        #流 控制台输出日志
        console = logging.StreamHandler()
        logger.addHandler(console)
        logger.debug("info")
        '''

        #文件名
        #当前文件路径
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir + "\\" + log_file
        #print(log_name)

        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        #设置输出log等级
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s ---> %(funcName)s %(lineno)d : %(levelname)s ---> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        #self.logger.debug("test1234")
        

    def get_log(self):
        return self.logger
    
    def close_handle(self):
        #关闭
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()
    
if __name__ == "__main__":
    user = UserLog()
    log = user.get_log()
    log.debug("testtest")
    user.close_handle()