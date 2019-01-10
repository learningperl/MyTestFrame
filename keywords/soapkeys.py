# -*- coding: UTF-8 -*-
import json, jsonpath
from common import logger
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import


class SOAP:
    """
        创建一个webservice接口请求的关键字类
    """

    def __init__(self, writer):
        # 文档标准
        self.doctor = None
        # client请求
        self.client = None
        # 保存wsdl文档地址
        self.wsdlurl = ''
        # 请求头
        self.header = {}
        # 保存的参数
        self.params = {}
        # 结果
        self.result = ""
        # 解析后的json字典
        self.jsonres = None
        # 写入结果的excel
        self.writer = writer

    # 添加校验的参数
    def adddoctor(self, targetNamespace, XMLSchema='', location=''):
        if XMLSchema == '':
            XMLSchema = 'http://www.w3.org/2001/XMLSchema'

        if location == '':
            location = 'http://www.w3.org/2001/XMLSchema.xsd'

        imp = Import(XMLSchema, location=location)
        # 添加命名空间，
        imp.filter.add(targetNamespace)
        self.doctor = ImportDoctor(imp)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    # 设置描述文档地址
    def setwsdl(self, url):
        self.wsdlurl = url
        try:
            self.client = Client(url, doctor=self.doctor, headers=self.header)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    def addheader(self, key, value):
        value = self.__getparams(value)
        self.header[key] = value
        try:
            self.client = Client(self.wsdlurl, doctor=self.doctor, headers=self.header)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    def removeheader(self, key):
        try:
            self.header.pop(key)
            self.client = Client(self.wsdlurl, doctor=self.doctor, headers=self.header)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    def callmethod(self, method, param=''):
        try:
            param = self.__getparams(param)
            if not param == '':
                p = param.split('、')

            if param == '':
                self.result = self.client.service.__getattr__(method)()
            else:
                self.result = self.client.service.__getattr__(method)(*p)

            self.jsonres = json.loads(self.result)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # 定义断言相等的关键字，用来判断json的key对应的值和期望值相等
    def assertequals(self, jsonpaths, value):
        res = 'None'
        print(self.jsonres)
        try:
            res = str(jsonpath.jsonpath(self.jsonres, jsonpaths)[0])
        except Exception as e:
            logger.exception(e)

        value = self.__getparams(value)

        print(type(res))
        print(type(value))

        if res == str(value):
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return True
        else:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return False

    # 定义保存一个json值为参数的关键字
    def savejson(self, key, p):
        res = ''
        print(self.jsonres)
        try:
            res = self.jsonres[key]
        except Exception as e:
            logger.exception(e)

        self.params[p] = res
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
        return True

    # 获取参数里面的值
    def __getparams(self, s):
        # logger.info(self.params)
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s
