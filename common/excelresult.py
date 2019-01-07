# coding:utf8

from common.Excel import Reader
from common import logger


class Res:
    """
    统计Excel用例执行结果信息
    powered by William
    2018-11-6
    copyright:testingedu.com.cn
    """
    def __init__(self):
        # 用于记录所有模块分组信息名称
        self.sumarry = {}

    def get_res(self, result_path):
        # 用于记录执行结果，逻辑为，只要分组中出现一个失败用例，则认为该分组执行失败，与flag联合使用。
        self.sumarry.clear()
        status = "Fail"
        # 标识是否有失败
        flag = True
        # 统计测试用例集的用例总条数
        totalcount = 0
        # 统计所有用例中通过用例的条数数
        totalpass = 0

        reader = Reader()
        reader.open_excel(result_path)
        reader.readline()
        line = reader.readline()
        self.sumarry['runtype'] = line[1]
        self.sumarry['title'] = line[2]
        self.sumarry['starttime'] = line[3]
        self.sumarry['endtime'] = line[4]
        # 获取所有sheet页面
        for n in reader.get_sheets():
            # logger.info(n)
            # 从第一个页面开始解析
            reader.set_sheet(n)
            # 获取sheet的行数，用来遍历
            row = reader.rows
            # 设置从第二行开始读
            reader.r = 1

            # 遍历sheet里面所有用例
            for i in range(1, row):
                line = reader.readline()
                # logger.info(line)
                # 查找记录了分组信息的行
                # 如果第一列（分组信息）和第二列（类别或用例名）不同时为空,则不是用例，执行非用例的操作
                if not (line[0] == '' and line[1] == ''):
                    pass

                # 非用例行判断结束
                # 第一列信息和第二列信息均为空的行，即用例行，这时开始进行用例数、通过数、状态的统计。
                else:
                    # 判断执行结果列，如果为空，将flag置为false,视为该行有误，不纳入用例数量计算
                    if len(line) < 7 or line[7] == '':
                        flag = False
                    # 执行结果不为空，则将用例统计数自增
                    else:
                        totalcount = totalcount + 1
                        # logger.info(line)
                        # 如果通过，则通过数和总通过数均自增
                        if line[7] == "PASS":
                            totalpass += 1
                        else:
                            # 出现了用例执行结果不是PASS的情况，则视为当前分组执行失败。
                            flag = False
            # for循环结束

        # 所有用例执行概况
        # logger.info(totalpass)
        # 计算执行通过率
        if flag:
            status = "Pass"

        # 计算通过率
        try:
            p = int(totalpass * 10000 / totalcount)
            passrate = p / 100
        except Exception as e:
            passrate = 0.0
            logger.exception(e)

        # 用例总数
        self.sumarry["casecount"] = str(totalcount)
        # 通过率
        self.sumarry["passrate"] = str(passrate)
        self.sumarry['status'] = status
        # logger.info(self.sumarry)
        return self.sumarry


if __name__ == '__main__':
    res = Res()
    r = res.get_res('../lib/results/result-HTTP接口用例.xls')
    print(r)
