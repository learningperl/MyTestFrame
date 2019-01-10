# -*- coding: UTF-8 -*-
from selenium import webdriver
import os, time, traceback
from common import logger
from selenium.webdriver.common.action_chains import ActionChains


class Web:
    """
        创建一个web自动化的关键字类
    """

    # 构造函数，用来创建实例变量，初始化一些代码
    def __init__(self, writer):
        # 初始化浏览器对象的实例变量
        # 实例变量用来保存打开的浏览器
        self.driver = None
        # 写入excel执行结果
        self.writer = writer
        # 保存参数
        self.params = {}

    # 定义函数，专门用来打开浏览器
    def openbrowser(self, b='', dpath='', t=''):
        """
        :param b: 浏览器类型：cc,ff,ie
        :param dpath: webdriver的地址
        :param t: 隐式等待的实际
        :return: 返回操作浏览器的driver
        """
        if t == '':
            t = 10

        try:
            t = int(t)
        except:
            t = 10

        if dpath == '':
            dpath = './lib/'

        if b == 'cc' or b == '':
            dpath += 'chromedriver'
            # 创建一个ChromeOptions的对象
            option = webdriver.ChromeOptions()
            # 去掉提示条的配置
            option.add_argument('disable-infobars')
            # 获取用目录
            try:
                # 异常处理，如果获取到，就使用获取到路径
                userdir = os.environ['USERPROFILE']
            except Exception as e:
                # 如果没有获取到，就使用默认的Administrator路径
                # 打印异常信息
                # traceback.print_exc()
                userdir = 'C:\\Users\\Administrator'

            userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
            userdir = '--user-data-dir=' + userdir
            # 添加用户目录
            option.add_argument(userdir)
            # 调用谷歌浏览器
            self.driver = webdriver.Chrome(executable_path=dpath, options=option)
            # 设置默认等待时间
            self.driver.implicitly_wait(t)
            self.driver.maximize_window()
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return self.driver

        if b == 'ff':
            dpath += 'geckodriver'
            self.driver = webdriver.Firefox(executable_path=dpath)
            # 设置默认等待时间
            self.driver.implicitly_wait(t)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return self.driver

        if b == 'ie':
            dpath += 'IEDriverServer'
            self.driver = webdriver.Ie(executable_path=dpath)
            # 设置默认等待时间
            self.driver.implicitly_wait(t)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return self.driver

    # 打开url
    def openurl(self, url):
        self.driver.get(url)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    # 点击关键字，根据xpath定位
    def click(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    # 向输入框输入的关键字，根据xpath定位
    def inputtext(self, xpath, value):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(value)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    # 关闭浏览器
    def quit(self):
        self.driver.quit()
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    # 强制等待
    def sleep(self, t):
        try:
            t = int(t)
        except:
            t = 1
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))

        time.sleep(t)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    # 根据窗口顺序切换窗口
    def switchwindow(self, idx):
        try:
            idx = int(idx)
        except Exception as e:
            idx = 0
            logger.warn('switchwindow参数错误：')
            logger.exception(e)

        handles = self.driver.window_handles
        try:
            self.driver.switch_to.window(handles[idx])
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def closewindow(self, cidx, oidx):
        """
        根据窗口id，关闭窗口，并切换到将要操作的窗口
        :param cidx: 需要关闭的窗口id
        :param oidx: 需要切换到的窗口id
        :return: 无
        """
        try:
            # 如果需要关闭的id输入错误，则直接结束
            cidx = int(cidx)
        except:
            cidx = 0
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

        # 默认切回第0个参数
        try:
            oidx = int(oidx)
        except Exception as e:
            oidx = 0
            logger.warn('closewindow参数错误：')
            logger.exception(e)

        handles = self.driver.window_handles
        try:
            # 切换到要关闭的窗口
            self.driver.switch_to.window(handles[cidx])
            # 关闭窗口
            self.driver.close()
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            # 切换到关闭后，需要操作的窗口
            self.driver.switch_to.window(handles[oidx])
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def __find_element(self, locator):
        """
        内部用来查找元素的方法
        支持使用三种主流查找方式
        :param locator: 支持输入xpath，id，content-desc
        :return:
        """
        try:
            if locator.startswith('/'):
                ele = self.driver.find_element_by_xpath(locator)
            else:
                try:
                    # 尝试用id定位
                    ele = self.driver.find_element_by_id(locator)
                except:
                    try:
                        # 尝试用name定位
                        ele = self.driver.find_element_by_name(locator)
                    except:
                        return None
        except Exception as e:
            logger.exception(e)
            return None
        return ele

    def intoiframe(self, locator):
        """
        通过定位到iframe，再进入iframe
        该关键字给同学们提供了一种多定位方式的实例，
        有具体需求的同学，可以参考该关键字实现方式
        :param locator: 元素的定位器（支持id，name，xpath）
        :return: 无
        """
        ele = self.__find_element(locator)
        try:
            # 根据定位，切换iframe
            self.driver.switch_to.frame(ele)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            # 定位失败，则写入失败信息
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def outiframe(self):
        """
        切回默认页面
        :return: 无
        """
        self.driver.switch_to.default_content()
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    def hover(self, xpath):
        """
        根据xpath，找到元素，并将鼠标悬停到元素
        该关键字自动化过程中，如果认为移动了鼠标可能导致悬停失败
        该关键字也可以用于页面滚动，但不一定都能滚动成功
        :param xpath: 元素的xpath
        :return:
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(ele).perform()
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False

    def scroll(self, x, y):
        """
        使用js滚动，既可以横向，也可以纵向滚动
        该方法使用的是scrollBy，增量式滚动
        :param x: 横向滚动距离
        :param y: 纵向滚动距离
        :return: 无
        """

        # 此处坐标直接使用字符串，因为js需要拼成字符串
        js = 'window.scrollBy(' + str(x) + ',' + str(y) + ');'
        try:
            self.driver.execute_script(js)
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def excutejs(self, js):
        """
        封装了默认执行js的方法
        :param js: 需要执行的标准js语句
        :return: 无
        """
        try:
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False

    def uploadfile(self, xpath, filepath):
        """
        根据xpath，找到元素
        使用send_keys上传文件
        :param xpath: 元素的xpath
        :param filepath: 需要上传文件的全路径
        :return: 无
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False
        try:
            ele.send_keys(filepath)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def gettitle(self):
        """
        获取当前窗口的title，并在系统中保存一个名叫title的变量
        在支持关联的关键字中，可以使用{title}，来调用它的值
        :return: 无
        """
        title = self.driver.title
        self.params['title'] = title
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    def gettext(self, xpath):
        """
        获取当前xpath定位元素的文本，并在系统中保存一个名叫text的变量
        在支持关联的关键字中，可以使用{text}，来调用它的值
        :param xpath: 元素的xpath
        :return: 无
        """
        self.params['text'] = ''
        try:
            text = self.driver.find_element_by_xpath(xpath).text
            self.params['text'] = text
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def assertequals(self, param, value):
        """
        定义断言相等的关键字，用来判断前后的值是否一致
        :param param: 需要校验的参数
        :param value: 需要校验的值
        :return: 无
        """
        param = self.__getparams(param)
        value = self.__getparams(value)
        if str(param) == str(value):
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(param))
            return True
        else:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(param))
            return False

    # 获取参数里面的值
    def __getparams(self, s):
        logger.info(self.params)
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s
