import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from common.case_result import CaseResult
report_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'report')


class SendEmail:

    def __init__(self,pass_list,fail_list):
            self.pass_list = pass_list
            self.fail_list = fail_list
            self.case_result = CaseResult()

    def get_new_file(self):
        lists = os.listdir(report_dir)  # 获取测试报告所在目录的所有文件
        lists.sort(key=lambda fn:os.path.getmtime(report_dir + '\\' + fn))  # 将所有文件正序排列
        file_path = os.path.join(report_dir,lists[-1])  # 获取最新的文件路径
        return file_path

    # 定义一个可以发送附件的发送邮件的方法
    def send_email(self):
        # 设置邮箱信息
        smptserver = 'smtp.qq.com'  # 发送邮件的服务器地址
        user = '972246473@qq.com'  # 登录邮箱的用户名
        password = 'hpvyradmzmsvbfdg'  # 开启smpt服务的密码
        sender = '972246473<972246473@qq.com>'  # 发件方的邮箱地址
        receiver = ['dehao.zeng@lvyuetravel.com']  # 收件方邮箱地址
        subject = '发送邮件测试'  # 邮件主题
        email_content = self.case_result.case_result(self.pass_list,self.fail_list)  # 邮件正文
        new_file = self.get_new_file()  # 邮件附件

        # 创建一个带附件的实例
        msg = MIMEMultipart()

        # 添加邮件头
        msg['subject'] = subject
        msg['from'] = sender
        msg['to'] = ';'.join(receiver)

        # 添加邮件正文信息
        part_content = MIMEText(email_content,_subtype='plain',_charset='utf-8')
        msg.attach(part_content)

        '''
        # 添加邮件附件信息（excel文件）
        part_file = MIMEApplication(open(new_file,'rb').read())
        part_file.add_header("Content-Disposition", "attachment", filename="testresult.xls")
        msg.attach(part_file)
        '''
        # 添加邮件附件信息（HTML文件-测试报告）
        # 构建附件1
        att1 = MIMEText(open(new_file,'rb').read().decode('utf-8'))
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment;filename="Platform Notice Test Result.html"'
        msg.attach(att1)



        # 连接服务器发送邮件
        server = smtplib.SMTP()
        server.connect(smptserver)
        server.login(user,password)
        server.sendmail(sender,receiver,msg.as_string())
        server.close()

if __name__ == '__main__':
    pass_list = [1,3,5,7,9]
    fail_list = [2,4,6,8]
    report_dir = "E:\\myproject\\lvyue_test\\lvyue_platform\\report"
    send_email = SendEmail(pass_list,fail_list)
    send_email.send_email()








