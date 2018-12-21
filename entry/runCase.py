# -*- coding: UTF-8 -*-
from common.Excel import Reader,Writer
from keywords.httpkeys import HTTP
import inspect


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
    http = HTTP(writer)
    reader.open_excel('../lib/cases/HTTP接口用例.xls')
    writer.copy_open('../lib/cases/HTTP接口用例.xls', '../lib/results/result-HTTP接口用例.xls')
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
                func = geffunc(line, http)
                lenargs = getargs(func)
                run(func, lenargs, line)

    writer.save_close()


runCases()
