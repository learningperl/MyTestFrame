# -*- coding: UTF-8 -*-
<<<<<<< HEAD
import requests, json
=======

>>>>>>> be01c1d6343e415d07f4ebeb2da7a7063144f4e9


# 创建一个http接口请求的关键字类
class HTTP:

    # 构造函数，实例化实例变量
    def __init__(self):
        # 创建session对象，模拟浏览器的cookie管理
        self.session = requests.session()
        # 存放json解析后的结果
        self.jsonres = {}
        # 用来保存所需要的数据，实现关联
        self.params = {}
<<<<<<< HEAD

    # 定义post实例方法，用来发送post请求
=======
		
		
	# 定义post实例方法，用来发送post请求
>>>>>>> be01c1d6343e415d07f4ebeb2da7a7063144f4e9
    def post(self, path, data=None):
        # 如果需要传参，就调用post，传递data
        if data is None:
            result = self.session.post(path)
        else:
            # 替换参数
            data = self.__getparams(data)
            # 转为字典
            data = self.__todict(data)
            # 发送请求
            result = self.session.post(path, data=data)

        self.jsonres = json.loads(result.text)
        print(self.jsonres)
<<<<<<< HEAD

    # 定义断言相等的关键字，用来判断json的key对应的值和期望值相等
    def assertequals(self, key, value):
        if str(self.jsonres[key]) == str(value):
            print('PASS')
        else:
            print('FAIL')

    # 给头添加一个键值对的关键字
    def addheader(self, key, value):
        value = self.__getparams(value)
        self.session.headers[key] = value

    # 定义保存一个json值为参数的关键字
    def savejson(self, p, key):
        self.params[p] = self.jsonres[key]
        print(self.params['t'])

    # 获取参数里面的值
    def __getparams(self, s):
        print(self.params)
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
            httpparam[p[0]] = p[1]

        return httpparam
=======
>>>>>>> be01c1d6343e415d07f4ebeb2da7a7063144f4e9
