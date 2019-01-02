# -*- coding: UTF-8 -*-
from common.Excel import Reader,Writer
from keywords.httpkeys import HTTP
from keywords.soapkeys import SOAP
import inspect
from common import config
from common.mysql import Mysql
from common.excelresult import Res
from common.mail import Mail


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
    reader = Reader()
    writer = Writer()
    soap = SOAP(writer)
    reader.open_excel('./lib/cases/SOAP接口用例.xls')
    writer.copy_open('./lib/cases/SOAP接口用例.xls', './lib/results/result-SOAP接口用例.xls')
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
                print(line)
                writer.row = i
                func = geffunc(line, soap)
                lenargs = getargs(func)
                run(func, lenargs, line)

    writer.save_close()


if __name__ == '__main__':
    config.get_config('./lib/conf/conf.txt')
    # logger.info(config.config)
    mysql = Mysql()
    mysql.init_mysql('./lib/conf/userinfo.sql')
    runCases()
    res = Res()
    r = res.get_res('./lib/results/result-HTTP接口用例.xls')
    text = config.config['mailtext']
    if r['status'] == 'PASS':
        text = text.replace('status',r['status'])
    else:
        text = text.replace('<font style="font-weight: bold;font-size: 14px;color: #00d800;">status</font>','<font style="font-weight: bold;font-size: 14px;color: red;">Fail</font>')

    text = text.replace('passrate', r['passrate'] + '%')
    text = text.replace('casecount', r['casecount'])
    print(text)
    mail = Mail()
    mail.send(text)



