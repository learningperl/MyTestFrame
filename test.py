# -*- coding: UTF-8 -*-
import threading,os,time
from keywords.appkeys import APP
import datetime


# t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(t)

m = 200
v = 30
mv = m/v
print(mv)
print('abc%.2fde' % mv)

# def run(cmd):
#     res = os.system(cmd)
#     print('子线程')
#     return res


# # c = 'node E:\\Appium-desktop\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
# c = 'netstat -aon | findstr 4723 | findstr  LISTENING'
# r = run(c)
# print(r.__str__())

# # 创建一个线程
# th = threading.Thread(target=run, args=(c,))
# # 开始执行线程
# th.start()
# print('主线程')

# cmd = 'netstat -aon | findstr 472'
# res = run(cmd)
# print(res)

# app = APP(None)
# app.runappium('E:\\appium-desktop','4777',5)
# app.runapp('{"platformName": "Android",  "platformVersion": "6.0.1",  "deviceName": "127.0.0.1:7555",  "appPackage": "com.tencent.mm","appActivity": ".ui.LauncherUI", "noReset": "true"}',6)
# time.sleep(5)
# app.swipe('250,140','250,480')
# app.click('com.tencent.mm:id/ge')
# time.sleep(5)
# app.click('美食')
# time.sleep(2)
# app.click('请输入商家或商品名称')
# time.sleep(2)
# app.inputtext('请输入商家或商品名称','鸡腿')
# time.sleep(2)
# app.longpress('鸡腿','2')
# time.sleep(5)
# app.close()
