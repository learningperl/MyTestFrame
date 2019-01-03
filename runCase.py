# -*- coding: UTF-8 -*-
from common.Excel import Reader, Writer
from keywords.httpkeys import HTTP
from keywords.soapkeys import SOAP
from keywords.webkeys import Web
import inspect, sys
from common import config
from common.mysql import Mysql
from common.excelresult import Res
from common.mail import Mail
from common import logger

# 运行的相对路径
path = '.'
# 用例路径
casepath = ''
resultpath = ''


# 反射获取关键字
def geffunc(line, http):
    func = None
    try:
        func = getattr(http, line[3])
    except Exception as e:
        print(e)

    return func


# 反射获取参数
def getargs(func):
    if func:
        args = inspect.getfullargspec(func).__str__()
        args = args[args.find('args=') + 5:args.find(', varargs')]
        args = eval(args)
        args.remove('self')
        l = len(args)
        return l
    else:
        return 0


# 运行一条用例
def run(func, lenargs, line):
    # 如果没有这个函数，就不执行
    if func is None:
        return

    if lenargs < 1:
        func()
        return

    if lenargs < 2:
        func(line[4])
        return

    if lenargs < 3:
        func(line[4], line[5])
        return

    if lenargs < 4:
        func(line[4], line[5], line[6])
        return

    print('error：目前只支持3个参数的关键字')


# 运行用例
def runCases():
    global casepath,resultpath
    reader = Reader()
    writer = Writer()
    web = Web(writer)
    reader.open_excel(casepath)
    writer.copy_open(casepath, resultpath)
    sheetname = reader.get_sheets()
    for sheet in sheetname:
        # 设置当前读写的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        # 默认写第7列
        writer.clo = 7

        for i in range(reader.rows):
            line = reader.readline()
            # 如果第一列或者第二列有内容，就是分组信息，不运行
            if len(line[0]) > 0 or len(line[1]) > 0:
                pass
            else:
                logger.info(line)
                writer.row = i
                func = geffunc(line, web)
                lenargs = getargs(func)
                run(func, lenargs, line)

    writer.save_close()


if __name__ == '__main__':
    try:
        casepath = sys.argv[1]
    except:
        casepath = ''

    # 为空，则使用默认的
    if casepath == '':
        casepath = path + '/lib/cases/web自动化用例.xls'
        resultpath = path + '/lib/results/result-web自动化用例.xls'
    else:
        # 如果是绝对路径，就使用绝对路径
        if casepath.find(':') >= 0:
            #获取用例文件名
            resultpath = path + '/lib/results/result-' + casepath[casepath.rfind('\\')+1:]
        else:
            logger.error('非法用例路径')

    config.get_config(path + '/lib/conf/conf.txt')
    # logger.info(config.config)
    mysql = Mysql()
    mysql.init_mysql(path + '/lib/conf/userinfo.sql')
    runCases()
    res = Res()
    r = res.get_res(resultpath)
    text = config.config['mailtext']
    if r['status'] == 'Pass':
        text = text.replace('status', r['status'])
    else:
        text = text.replace('<font style="font-weight: bold;font-size: 14px;color: #00d800;">status</font>',
                            '<font style="font-weight: bold;font-size: 14px;color: red;">Fail</font>')

    text = text.replace('passrate', r['passrate'] + '%')
    text = text.replace('casecount', r['casecount'])
    print(text)
    mail = Mail()
    mail.send(text)
