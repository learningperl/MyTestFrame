# -*- coding: UTF-8 -*-

# def __todict(s):
#     httpparam = {}
#     # 分割参数个数
#     param = s.split('&')
#     for ss in param:
#         # 把键值对分开
#         p = ss.split('=')
#         if len(p) > 1:
#             httpparam[p[0]] = p[1]
#         else:
#             httpparam[p[0]] = ''
#
#     return httpparam
#
# session = requests.session()
# session.headers[
#     'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
# session.headers['Content-type'] = 'application/x-www-form-urlencoded'
# # print(res.text)
# # session.headers['x-udid'] = 'ACCha1aUqA6PTsEjcylWGx8HHM3feFPytFg=|1544611343'
# # 获取一个udid
# print(session.cookies)
# res = session.post('https://www.zhihu.com/udid', data=None)
# print(res.text)
# print(session.cookies)
# res = session.get('http://www.zhihu.com/api/v3/oauth/captcha?lang=en')
# print(res.text)
# session.headers['x-zse-83'] = '3_1.1'
# print(session.cookies)
# print(session.headers)
# res = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',
#                    data='ToOk0KPwMtBtNXtzltBlMKpxBduq0PQzppOk0KPwMtBtNX0x1hBlMK6z0p9a01AzwLAlMK-pNsauCle2hdQwQGohEobaMc8k-9uxA-dyUXeuD6dpisaxMxP2NlfuKx8k1OQz82LkQcraOs8k1cbkKG5xU6v4NsqxsdAzMLP1PxNa058lw2bl6P_kToQvKkuxwpQw80_l0xQvTobl-cNw6dKk0xbbRoQwmkepNKpxMtvr6TQxolBlMK6w02RdP6uypDBjHxPwclbf0lA1kXQ1QGohSwr_Ogrkj18lOOolLo9a0_vzwpR10ptyOxNa0oA1u2R1N6d1clbf0-v3lXd2I601BxNa0_8k1-8lLCoxLcQb00rwigemAD_lScbuQwNwmwux8DKwclbf90QvlTuxDtPw')
# print(res.text)
# res = session.get('https://www.zhihu.com/logout',data=None)
# print(res.text)

# from suds.client import Client
# from suds.xsd.doctor import ImportDoctor, Import
#
# imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# # 添加命名空间，
# imp.filter.add('http://WebXml.com.cn/')
# doctor = ImportDoctor(imp)
#
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl', doctor=doctor)
# res = client.service.auth()
# print(res)
# header = {}
# header['token'] = 'ee905617920a4c498264cd7d567536c0'
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl', doctor=doctor, headers=header)
# s = 'Tester、123456'
# s = s.split('、')
# m = 'login'
# # 反射获取函数client.service.__getattr__(m)
# res = client.service.__getattr__(m)(*s)
# # res = client.service.login(*s)
# print(res)
# res = client.service.logout()
# print(res)


# from keywords.soapkeys import SOAP
#
# soap = SOAP()
# soap.adddoctor('')
# soap.setwsdl('http://112.74.191.10:8081/inter/SOAP?wsdl')
# soap.callmethod('auth')
# soap.savejson('token','token')
# soap.addheader('token','{token}')
# soap.callmethod('login','Tester、123456')
# soap.callmethod('logout')

# import requests
#
# session = requests.session()
#
# result = session.get('https://ke.qq.com/course/list/特斯汀学院?tuin=3ec2bac8')
# print(result.text)


