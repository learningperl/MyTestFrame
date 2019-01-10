# -*- coding: UTF-8 -*-
from appium import webdriver
from common import logger
from appium.webdriver.common.touch_action import TouchAction
import os, threading, time,traceback


class APP:
    """
        创建一个APP自动化的关键字类
    """

    def __init__(self, writer):
        # 初始化浏览器对象的实例变量
        # 实例变量用来保存打开的app
        self.driver = None
        # 写入excel执行结果
        self.writer = writer
        # 保存参数
        self.params = {}
        # 保存appium服务端口
        self.port = ''

    def runappium(self, path, port, t):
        """
        多线程运行appium服务
        :param path: appium-desktop的安装路径
        :param port: 服务的端口
        :param t: 等待时间，默认5s
        :return: 无
        """

        # 多线程函数，用来执行cmd命令
        def run(cmd):
            res = os.system(cmd)
            return res

        if port == '':
            port = '4723'

        # 保存端口，启动APP是需要用到
        self.port = port

        # 查看端口是否被占用
        cmd = 'netstat -aon | findstr ' + port + ' | findstr LISTENING'
        res = run(cmd)
        # cmd执行有结果就是0，没有结果就是1
        if str(res) == '0':
            logger.error('端口已被占用')
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, '端口已被占用')
            return False
        else:
            # 启动appium
            cmd = 'node ' + path + '\\resources\\app\\node_modules\\appium\\build\\lib\\main.js -p ' + port
            th = threading.Thread(target=run, args=(cmd,))
            th.start()
            try:
                t = int(t)
            except:
                t = 5
            time.sleep(t)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True

    def runapp(self, c, t):
        """
        运行APP的关键字
        :param c: 启动APP的配置，标准的json字符串就可以
        :param t: 隐式等待的实际
        :return: 操作APP的driver对象
        """
        # 默认配置
        conf = {
            "platformName": "Android",
            "platformVersion": "4.4.2",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.mobileqq",
            "appActivity": ".activity.SplashActivity",
            "noReset": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true"
        }
        # 获取要启动APP的配置，并写入到默认配置里面
        try:
            c = eval(c)
            for key in c:
                conf[key] = c[key]
        except Exception as e:
            logger.warn('app配置错误，请检查')
            logger.exception(e)

        # 多个设备时指定连接设备
        conf['udid'] = conf['deviceName']
        # 确保设备是连上的
        try:
            os.system('adb connect ' + conf['udid'])
        except:
            pass

        try:
            t = int(t)
        except:
            t = 10
        # 通过remote方法连接appium服务，并且启动APP
        self.driver = webdriver.Remote("http://localhost:" + self.port + "/wd/hub", conf)
        # 设置隐式等待
        self.driver.implicitly_wait(t)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    def close(self):
        """
        关闭appium服务，appium是通过node.exe进程启动
        :return: 无
        """
        try:
            os.system('taskkill /F /IM node.exe')
        except:
            pass

        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    def __find_element(self, locator):
        """
        内部用来查找元素的方法
        支持使用三种主流查找方式
        :param locator: 支持输入xpath，id，content-desc
        :return:
        """
        try:
            if locator.find(':id') > -1:
                ele = self.driver.find_element_by_id(locator)
            else:
                if locator.startswith('/'):
                    ele = self.driver.find_element_by_xpath(locator)
                else:
                    ele = self.driver.find_element_by_accessibility_id(locator)
        except Exception as e:
            logger.exception(e)
            return None
        return ele

    def click(self, locator):
        """
        点击方法，找到元素并点击
        :param locator: 元素定位器
        :return:
        """
        time.sleep(1)
        ele = self.__find_element(locator)
        try:
            ele.click()
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def inputtext(self, locator, value):
        time.sleep(1)
        ele = self.__find_element(locator)
        try:
            ele.send_keys(value)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def tryinput(self, locator, value):
        time.sleep(1)
        ele = self.__find_element(locator)
        try:
            ele.send_keys(value)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')

        return True

    def swipe(self, p1, p2):
        """
        从p1坐标点滑动到p2坐标点
        :param p1: 起始坐标点 111,22
        :param p2: 终止坐标点 333,22
        :return:
        """
        try:
            p1 = p1.split(',')
            x1 = int(p1[0])
            y1 = int(p1[1])
            p2 = p2.split(',')
            x2 = int(p2[0])
            y2 = int(p2[1])

            TouchAction(self.driver).press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def back(self):
        self.driver.back()
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    def sleep(self, t):
        try:
            t = int(t)
        except:
            t = 1

        time.sleep(t)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True
