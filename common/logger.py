# coding:utf8
import logging


class Logger:
    """
            powered by Mr Will
               at 2018-12-21
            用来格式化打印日志到文件和控制台
    """
    def __init__(self, path=None):
        self.path = '..'
        self.logger = None
        if not path is None:
            self.path = path
        # create logger
        # 这里可以修改开源模块的日志等级
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                            filename=self.path + "/lib/logs/all.log",
                            level=logging.ERROR)
        self.logger = logging.getLogger('frame log')
        self.logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # # add formatter to ch
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    # 打印debug级别日志
    def debug(self, ss):
        try:
            self.logger.debug(ss)
        except:
            return

    # 打印info级别日志
    def info(self, str):
        try:
            self.logger.info(str)
        except:
            return

    # 打印debug级别日志
    def warn(self, ss):
        try:
            self.logger.warning(ss)
        except:
            return

    # 打印error级别日志
    def error(self, ss):
        try:
            self.logger.error(ss)
        except:
            return

    # 打印异常日志
    def exception(self, e):
        try:
            self.logger.exception(e)
        except:
            return


# 调试
if __name__ == '__main__':
    logger = Logger()
    logger.info('test')
