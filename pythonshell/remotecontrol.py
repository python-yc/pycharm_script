# -*- coding: utf-8 -*-
import paramiko
import os

class RemoteContol:
    # def __init__(self, ip, port=22, username="paas", userpwd="QAZ123.0"):
    #     self.ip = ip
    #     self.port = port
    #     self.username = username
    #     self.userpwd = userpwd

    def up_load_file(self, ip, port, username, userpwd):
        """从windows上传文件到linux上"""
        t = paramiko.Transport((ip, port))
        t.connect(username=username, password=userpwd)
        sftp = t.open_sftp_client()
        local_path = os.path.join('D:/a.txt')
        remote_path = '/home/paas/' + os.path.basename(local_path)
        sftp.put(local_path=local_path, remotepath=remote_path)
        t.close()


if __name__ == '__main__':
    rc = RemoteContol()
    rc.up_load_file('192.168.1.125', 22, 'root', '123456')
