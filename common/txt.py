# coding:utf8
from common import logger


class Txt:
    """
        powered by Mr Will
           at 2018-12-21
        用来读写文件
    """

    # 构造函数打开txt
    def __init__(self, path, t='r', coding='utf8'):
        """
        初始化实例，打开一个txt文件
        :param path: txt的路径
        :param t: 打开文件的方式，r:只读(默认)；w:只写；rw:可读写
        :param coding: 打开文件的编码，默认utf8
        """
        self.data = []
        self.f = None
        if t == 'r':
            # 逐行读取
            for line in open(path, encoding=coding):
                self.data.append(line)
            # 去掉末尾换行
            for i in range(self.data.__len__()):
                # 处理非法字符
                self.data[i] = self.data[i].encode('utf-8').decode('utf-8-sig')
                self.data[i] = self.data[i].replace('\n', '')

            return

        if t == 'w':
            # 打开可读文件
            # a代表在末尾添加
            self.f = open(path, 'a', encoding=coding)
            return

        if t == 'rw':
            for line in open(path, encoding=coding):
                self.data.append(line)
            # 去掉换行
            for i in range(self.data.__len__()):
                # 处理非法字符
                self.data[i] = self.data[i].encode('utf-8').decode('utf-8-sig')
                self.data[i] = self.data[i].replace('\n', '')

            self.f = open(path, 'a', encoding=coding)
            return

    # 读取
    def read(self):
        """
        将txt文件按行读取为列表
        :return: 返回txt所有内容的列表
        """
        return self.data

    def writeline(self, s):
        """
        往txt文件末尾写入一行
        :param s: 需要写入的内容，若要换行，请自己添加\n
        :return: 无
        """
        if self.f is None:
            logger.error('error：未打开可写入txt文件')
            return

        self.f.write(str(s))

    def save_close(self):
        '''
        写入文件后，必须要保存
        :return: 无
        '''
        if self.f is None:
            logger.error('error：未打开可写入txt文件')
            return

        self.f.close()


# 调试
if __name__ == '__main__':
    # 读取
    reader = Txt('../lib/conf/conf.txt')
    t = reader.read()
    print(t)

    # 写入
    writer = Txt('../lib/logs/all.log', t='w')
    writer.writeline('写入成功\n')
    writer.save_close()
