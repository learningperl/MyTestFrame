# -*- coding: UTF-8 -*-
import requests, json
from keywords.httpkeys import HTTP

# 创建HTTP实例对象，用来调用关键字
http = HTTP()
# 无token
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token为‘’
http.addheader('token', '')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token为‘a’
http.addheader('token', 'a')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token为‘aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa’
http.addheader('token', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token未授权
http.addheader('token', '109f1a34bdcf4785b6c70a9917d7a49d')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# 保存上一步的token
http.savejson('t', 'token')
http.addheader('token', '{t}')
print(http.session.headers)
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '201')

# 登录一个用户，并查询他的用户信息
http.post('http://112.74.191.10:8081/inter/HTTP/login', 'username=Tester&password=123456')
http.assertequals('status', '200')
http.savejson('id', 'userid')
http.post('http://112.74.191.10:8081/inter/HTTP/getUserInfo', 'id={id}')
http.assertequals('status', '200')
http.post('http://112.74.191.10:8081/inter/HTTP/logout')
http.assertequals('status', '200')
