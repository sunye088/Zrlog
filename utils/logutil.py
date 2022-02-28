# 导入日志存放的路径

# 导入logging

import logging
# 导入time
import os
import time

# 导入os库
from config.settings import get_log_path

STREAM = True


# 设置日志工具类的类名
class LogUtil:
    def __init__(self):
        # 初始化日志对象，设置日志名称
        self.logger = logging.getLogger("logger")
        # 设置总的日志级别开关
        self.logger.setLevel(logging.DEBUG)
        # 避免日志重复
        if not self.logger.handlers:
            # 定义日志成名
            self.log_name = '{}.log'.format(time.strftime("%Y_%m_%d", time.localtime()))
            # 定义日志路径及文件名称
            self.log_path_file = os.path.join(get_log_path(),self.log_name)
            # 定义文件处理handler
            fh = logging.FileHandler(self.log_path_file, encoding='utf-8', mode='w')
            # 设置文件处理handler的日志级别
            fh.setLevel(logging.DEBUG)
            # 日志格式变量
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            # 设置打印格式
            fh.setFormatter(formatter)
            # 添加handler
            self.logger.addHandler(fh)
            # 光比handler
            fh.close()
            # 控制台输出
            if STREAM:
                # 定义控制台输出流handler
                fh_stream = logging.StreamHandler()
                # 控制台输出日志级别
                fh_stream.setLevel(logging.DEBUG)
                # 设置打印格式
                fh_stream.setFormatter(formatter)
                # 添加handler
                self.logger.addHandler(fh_stream)

    def log(self):
        # 返回定义好的logger对象，对外直接使用log函数即可
        return self.logger


# 其他程序可直接调用logger对象
logger = LogUtil().log()

if __name__ == '__main__':
    logger.info('test')
