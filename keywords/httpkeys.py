# -*- coding: UTF-8 -*-
import requests, json, jsonpath
from common import logger


class HTTP:
    """
        创建一个http接口请求的关键字类
    """
    # 构造函数，实例化实例变量
    def __init__(self,writer):
        # 创建session对象，模拟浏览器的cookie管理
        self.session = requests.session()
        # 存放json解析后的结果
        self.jsonres = {}
        # 用来保存所需要的数据，实现关联
        self.params = {}
        # 全局的url
        self.url = ''
        # 写入结果的excel
        self.writer = writer
        # 添加默认UA，模拟chrome浏览器
        self.session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        # 添加默认的请求Content-type
        self.session.headers['Content-type'] = 'application/x-www-form-urlencoded'

    # 设置地址
    def seturl(self,url):
        if url.startswith('http'):
            self.url = url
            self.writer.write(self.writer.row,self.writer.clo,'PASS')
            return True
        else:
            logger.error('error：url地址不合法')
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo+1, 'error：url地址不合法')
            return False

    # 定义post实例方法，用来发送post请求
    def post(self, path, data=''):
        """
        # 定义post实例方法，用来发送post请求
        :param path: url路径
        :param data: 键值对传参的字符串
        :return: 无返回值
        """
        try:
            if not path.startswith('http'):
                path = self.url + '/' + path

            # 如果需要传参，就调用post，传递data
            if data == '':
                result = self.session.post(path)
            else:
                # 替换参数
                data = self.__getparams(data)
                # 转为字典
                data = self.__todict(data)
                # 发送请求
                result = self.session.post(path, data=data)

            res = result.text
            try:
                res = res[res.find('{'):res.rfind('}') + 1]
            except Exception as e:
                logger.exception(e)

            self.jsonres = json.loads(res)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo+1, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # 定义断言相等的关键字，用来判断json的key对应的值和期望值相等
    def assertequals(self, jsonpaths, value):
        res = 'None'
        try:
            res = str(jsonpath.jsonpath(self.jsonres, jsonpaths)[0])
        except Exception as e:
            logger.exception(e)

        value = self.__getparams(value)

        if res == str(value):
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return True
        else:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return False

    # 给头添加一个键值对的关键字
    def addheader(self, key, value):
        value = self.__getparams(value)
        self.session.headers[key] = value
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(value))
        return True

    # 从头里面删除一个键值对
    def removeheader(self,key):
        self.session.headers.pop(key)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(key))
        return True

    # 定义保存一个json值为参数的关键字
    def savejson(self, key, p):
        res = ''
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
        logger.info(self.params)
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s

    # 将一个标准的URL地址参数转换为一个dict
    # username=Tester55&password=123456&ttt=ccccc
    # {'username':'Tester55','password':'123456','tttt':'ccccc'}
    def __todict(self, s):
        httpparam = {}
        # 分割参数个数
        param = s.split('&')
        for ss in param:
            # 把键值对分开
            p = ss.split('=')
            if len(p)>1:
                httpparam[p[0]] = p[1]
            else:
                httpparam[p[0]] = ''

        return httpparam
