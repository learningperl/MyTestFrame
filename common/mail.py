# coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from common import config,logger


class Mail:
    """
        powered by Mr Will
        at 2018-12-22
        用来获取配置并发送邮件
    """
    def __init__(self):
        self.mail_info = {}
        # 发件人
        self.mail_info['from'] = config.config['mail']
        self.mail_info['username'] = config.config['mail']
        # smtp服务器域名
        self.mail_info['hostname'] = 'smtp.' + config.config['mail'][
                                               config.config['mail'].rfind('@') + 1:config.config['mail'].__len__()]
        # 发件人的密码
        self.mail_info['password'] = config.config['pwd']
        # 收件人
        self.mail_info['to'] = str(config.config['mailto']).split(',')
        # 抄送人
        self.mail_info['cc'] = str(config.config['mailcopy']).split(',')
        # 邮件标题
        self.mail_info['mail_subject'] = config.config['mailtitle']
        self.mail_info['mail_encoding'] = config.config['mail_encoding']

    def send(self, text):
        # 这里使用SMTP_SSL就是默认使用465端口，如果发送失败，可以使用587
        smtp = SMTP_SSL(self.mail_info['hostname'])
        smtp.set_debuglevel(0)

        ''' SMTP 'ehlo' command.
        Hostname to send for this command defaults to the FQDN of the local
        host.
        '''
        smtp.ehlo(self.mail_info['hostname'])
        smtp.login(self.mail_info['username'], self.mail_info['password'])

        msg = MIMEText(text, 'html', self.mail_info['mail_encoding'])
        msg['Subject'] = Header(self.mail_info['mail_subject'], self.mail_info['mail_encoding'])
        msg['from'] = self.mail_info['from']

        logger.debug(self.mail_info)
        logger.debug(text)
        msg['to'] = ','.join(self.mail_info['to'])
        msg['cc'] = ','.join(self.mail_info['cc'])
        receive = self.mail_info['to']
        receive += self.mail_info['cc']

        try:
            smtp.sendmail(self.mail_info['from'], receive, msg.as_string())
            smtp.quit()
            logger.info('邮件发送成功')
        except Exception as e:
            logger.error('邮件发送失败：')
            logger.exception(e)


if __name__ == '__main__':
    config.get_config('../lib/conf/conf.txt')
    logger.debug(config.config)
    mail = Mail()
    html = '<html><style type="text/css">body{ background:#ffffff; margin:0 auto; padding:0; text-align:left; font-size:13px; font-family: "微软雅黑","宋体";}table{ font-size:13px; font-family: "微软雅黑","宋体";}.table_c{border:1px solid #ccc;border-collapse:collapse; }.table_c td{border:1px solid #ccc; border-collapse:collapse;}.table_b{border:1px solid #666;border-collapse:collapse; }.table_b td{ border-collapse:collapse; border:1px solid #ccc;}.table_b th{color:#fff; background:#666;}a:link{ color:#3366cc; font-weight:normal; }a:visited { color: #3366cc;}a:hover{ color:#000; }a:active { color:#3366cc; }td{ line-height:20px;}.case-group {border: 1px solid transparent;border-color: #ddd;line-height:5px;}.case-group a:link,a:hover{color:#0092fa;text-decoration:none;}.group-模拟器测试用例{margin: 10px;}.case-模拟器测试用例{height: 30px;}.case-case {border-top: 1px solid;border-color: #ddd;padding: 13px;word-wrap: break-word;}.statuclass{float:right;right:5%;position:relative;}.countclass{float:right;right:20%;position:relative;}.passclass{float:right;right:30%;position:relative;}.casename{position:relative;left:3%;}.righta{float:right;font-size:20px;}.case-file{border: 2px #8cbfff solid;border-radius: 5px;}</style><table width="650" ="0" cellspacing="0" align="center" cellpadding="0" style="border-radius: 15px;background-color: #f6f5f5;border: 1px #ffe4da solid;"><tbody><tr><td><table width="650" border="0" cellpadding="0" cellspacing="0" style="border-radius: 15px 15px 0 0;background-color: #ffffff;"><tbody><tr><td width="137"><img src="http://112.74.191.10/wp-content/uploads/2018/07/logo_middle.png" width="137" height="80"></td><td align="left" style="font-size: 13px;color: #999999;padding-top: 26px;right: 10px;position: relative;top: -10px;text-align:right;"><h style="font-size: 20px;font-family: cursive;line-height: 30px;color: #8cbfff;">Hi All ！ </h><br>此为来自特斯汀学院自动化小组测试邮件，请不要直接回复。</td></tr></tbody></table><br><table width="592" border="0" cellspacing="0" cellpadding="0" align="center"><tbody><tr><td style="font-size: 14px; color: 333333; font-weight: bold; padding-bottom:15px;">测试报告：<font color="ff6600">自动化测试用例</font></td></tr><tr><td style="border: 2px #8cbfff solid;border-radius: 5px;"><table width="572" border="0" align="center" class="table_c" style="border-collapse:collapse;margin: 10px;"><tbody><tr><td width="100" height="28" align="center" bgcolor="#ffe9e9" style="border:1px solid #ccc;">测试内容</td><td colspan="3" bgcolor="#FFFFFF" align="center" style="border:1px solid #ccc;"><h4 style="line-height: 1px;margin:0;">title</h4></td></tr><tr><td width="100" height="28" align="center" bgcolor="#ffe9e9" style="border:1px solid #ccc;">测试状态</td><td height="28" width="150" bgcolor="#FFFFFF" align="center" style="border:1px solid #ccc;"><font style="font-weight: bold;font-size: 14px;color: #00d800;">status</font></td><td width="100" height="28" align="center" bgcolor="#ffe9e9" style="border:1px solid #ccc;">类型</td><td height="28" bgcolor="#FFFFFF" align="center" style="border:1px solid #ccc;">runtype</td></tr><tr><td width="80" height="28" align="center" bgcolor="#ffe9e9" style="border:1px solid #ccc;">通过率</td><td height="28" bgcolor="#FFFFFF" align="center" style="border:1px solid #ccc;">passrate</td><td width="100" height="28" align="center" bgcolor="#ffe9e9" style="border:1px solid #ccc;">开始时间</td><td height="28" bgcolor="#FFFFFF" align="center" style="border:1px solid #ccc;">starttime</td></tr><tr><td width="80" height="28" align="center" bgcolor="#ffe9e9" style="border:1px solid #ccc;">总用例数</td><td height="28" bgcolor="#FFFFFF" align="center" style="border:1px solid #ccc;">casecount</td><td width="80" height="28" align="center" bgcolor="#ffe9e9" style="border:1px solid #ccc;">结束时间</td><td height="28" bgcolor="#FFFFFF" align="center" style="border:1px solid #ccc;">endtime</td></tr></tbody></table></td></tr><tr><td><table width="592" border="0" align="center" cellspacing="0" cellpadding="0" style="margin: 24px 0 10px 0;border-bottom: #e4e4e4 1px solid;"><tbody><tr><td style="font-size: 13px; line-height: 20px; color: #999999; padding-top: 6px;">如果您对本次邮件结果有任何疑问，请联系 <a href="http://wpa.qq.com/msgrd?v=3&uin=1052949192&site=qq&menu=yes" target="_blank" color="#666666">William：1052949192</a></a> 反馈。</td></tr></tbody></table></td></tr><td><table width="592" border="0" align="center" cellspacing="0" cellpadding="0" style="margin: 24px 0 16px 0;border-top: #e4e4e4 1px solid;"><tbody><tr><td style="font-size: 13px; line-height: 20px; color: #999999; padding-top: 6px;">感谢您的查阅。<font color="#666666">All Rights Reserved by 特斯汀 College. Designed and Developed by Mr. William.</font></a></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></body></html>'
    mail.send(html)
