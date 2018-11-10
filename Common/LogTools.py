#!/user/bin/env python
#!encoding=utf-8
import os
import time
import logging
from Common.PathTools import log_path

'''日志相关封装函数'''

class LogTools:
    def __init__(self):
        '''初始化'''
        #设置日志名称与路径
        self.logname='%s.log'%self._get_nowtime()
        self.logfile=os.path.join(log_path,self.logname)
        #创建log
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.format=logging.Formatter('[%(asctime)s]-[%(levelname)s]-%(message)s')

    def _get_nowtime(self):
        '''获取当天日期'''
        nowtime=time.strftime('%Y-%m-%d')
        return nowtime

    def _console(self,loglevel,message):
        '''
        设置本地与日志输出
        :param loglevel:日志等级
        :param message:输出msg
        '''
        # 创建一个FileHandler，用于本地日志输出
        fh=logging.FileHandler(self.logfile,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler，用于控制台输出
        sh=logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.format)
        self.logger.addHandler(sh)

        #通过判断level输出
        if loglevel=='info':
            self.logger.info("".join(["run:",message]))
        elif loglevel=='debug':
            self.logger.debug("".join(["run:",message]))
        elif loglevel=='warning':
            self.logger.warning("".join(["run:",message]))
        elif loglevel=='error':
            self.logger.error("".join(["run:",message]))

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def info(self,message):
        '''输出info信息'''
        self._console('info',message)

    def warning(self,message):
        '''输出warning信息'''
        self._console('warning',message)

    def debug(self,message):
        '''输出debug信息'''
        self._console('debug',message)

    def error(self,message):
        '''输出error信息'''
        self._console('error',message)


if __name__=="__main__":
    log=LogTools()
    log.info('123113123')