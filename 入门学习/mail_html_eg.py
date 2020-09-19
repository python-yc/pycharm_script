from email.mime.text import MIMEText
import smtplib
mail_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Title</title>
            </head>
            <body>
            
            <h1> 这是一封HTML格式邮件</h1>
            
            </body>
            </html>
            
            """
msg = MIMEText(mail_content,"html","utf-8")

#构造发送者地址和登录信息
from_addr = "15655982512@qq.com"
from_pwd = "saiofhaksfoyigadha"

# 构建邮件接收者信息
to_addr = "15655982512@qq.com"

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱的smtp地址是 smtp.qq.com

smtp_srv = "smtp.qq.com"

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)#SMTP协议默认端口25
    # 登录邮箱发送
    srv.login(from_addr,from_pwd)
    #发送邮件，三个参数
    # 1.发送地址
    # 2.接受地址，必须是list形式
    # 3.发送内容，作为字符串发送
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)






