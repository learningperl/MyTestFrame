# -*- coding: UTF-8 -*-

from common import logger, config
from common.mysql import Mysql
import requests


def __todict(s):
    httpparam = {}
    # 分割参数个数
    param = s.split('&')
    for ss in param:
        # 把键值对分开
        p = ss.split('=')
        if len(p) > 1:
            httpparam[p[0]] = p[1]
        else:
            httpparam[p[0]] = ''
    print(httpparam)
    return httpparam


# #
# config.get_config('../lib/conf/conf.txt')
# # logger.info(config.config)
# mysql = Mysql()
# mysql.init_mysql('C:\\Users\\Will\\Desktop\\userinfo.sql')


from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
doctor = ImportDoctor(imp)

client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl',doctor=doctor)
result = client.service.getWeatherbyCityName('长沙')
print(result)

