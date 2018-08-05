# 发邮件的库
import smtplib

# 邮件文本
from email.mime.text import MIMEText

# SMTP 服务器
SMTPServer = "smtp.163.com";

# 发邮件的地址
sender = "wan318413@163.com"

# 发送者邮件的密码（授权的密码）

passwd = "904817songjia"

# 设置发送的内容
message = "基本密码就是我"
# 转换成邮件文本
msg = MIMEText(message)

# 标题

msg["Subject"] = "来自我的问候"

# 发送者
msg["From"] = sender

# 创建 smtp服务器  相当于连接到别人的服务器上去

mailServer = smtplib.SMTP(SMTPServer, 25)

# 登录邮箱
mailServer.login(sender, passwd)

# 发送邮箱
mailServer.sendmail(sender, ["15711261792@163.com"], msg.as_string())


#退出邮箱
mailServer.quit()