"""
- FTP工作流程
    - 1.客户端连接远程主机的FTP服务器
    - 2.客户端输入用户名和密码（或者anonymous和电子邮件地址）
    - 3.客户端和服务器进行各种文件传输和信息查询操作
    - 4.客户端从远程FTP服务器退出，结束传输
"""
import ftplib
import os
import socket

#三部分精确表示在ftp服务器上的某一个文件
#很多公开ftp服务器访问会出错或者没有反应
HOST = "ftp.acc.umu.se"
DIR = "Public/EFLIB"
FILE = "README"

# 1.客户端连接远程主机上的FPT服务器
try:
    f = ftplib.FTP()
    #通过设置调试级别可以方便调试
    f.set_debuglevel(2)
    #连接主机地址
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("***Connected to host {0}".format(HOST))

# 2.客户端输入用户名和密码（或者anonymous和电子邮件地址）
try:
    #登录如果没有输入用户名信息，则默认使用匿名登录
    f.login()
except Exception as e:
    print(e)
    exit()
print("***Logged in as 'anonymous'")

# 3.客户端和服务器进行各种文件传输和信息查询操作
try:
    #更改当期那目录到指定目录
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("***Change dir to {0}".format(DIR))

try:
    #从FTP服务器上下载文件
    #第一个参数是ftp命令，第二个参数是回调函数
    #此函数的意思是，执行RETR命令，下载文件到本地后，运行回调函数
    f.retrbinary('RETR {0}'.format(FILE),open(FILE,'wb'.write()))
except Exception as e:
    print(e)
    exit()

# 4.客户端从远程FTP服务器退出，结束传输
f.quit()
