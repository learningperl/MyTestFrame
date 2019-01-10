# -*- coding: UTF-8 -*-
import unittest,sys
from BeautifulReport import BeautifulReport as bf
from myunittest import datadriven
from common import config
from common.mysql import Mysql
from common import logger

# 运行的相对路径
path = '.'
# 用例路径
casepath = ''
resultpath = ''

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(testWeb))
    # suite = unittest.defaultTestLoader.discover(".", pattern="baidu.py", top_level_dir=None)
    # # 生成执行用例的对象
    # runner = bf(suite)
    # runner.report(filename='./test.html', description='这个描述参数是必填的')

    try:
        casepath = sys.argv[1]
    except:
        casepath = ''

    # 为空，则使用默认的
    if casepath == '':
        casepath = path + '/lib/cases/HTTP接口用例.xls'
        resultpath = path + '/lib/results/result-HTTP接口用例.xls'
    else:
        # 如果是绝对路径，就使用绝对路径
        if casepath.find(':') >= 0:
            # 获取用例文件名
            resultpath = path + '/lib/results/result-' + casepath[casepath.rfind('\\') + 1:]
        else:
            logger.error('非法用例路径')

    config.get_config(path + '/lib/conf/conf.txt')
    # logger.info(config.config)
    mysql = Mysql()
    mysql.init_mysql(path + '/lib/conf/userinfo.sql')
    datadriven.getparams(casepath,resultpath)

    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(baidu))
    suite = unittest.defaultTestLoader.discover("./myunittest/", pattern="WebTest.py", top_level_dir=None)
    # 生成执行用例的对象
    runner = bf(suite)
    runner.report(filename='./test.html', description='这个描述参数是必填的')

