# -*- coding: UTF-8 -*-



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
		
		
	# 定义post实例方法，用来发送post请求
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
