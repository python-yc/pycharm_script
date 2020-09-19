# -*- coding: utf-8 -*-
import os

# https://www.cnblogs.com/wf-linux/archive/2018/08/01/9400354.html

# #获取系统环境变量  getenv() 效果
print(os.environ['PATH'])
print(os.getenv('PATH'))

#设置系统环境变量 putenv()
# os.environ['PATH'] += ':/home/sy/下载'

"""
os 常用方法

os.remove(‘path/filename’) 删除文件

os.rename(oldname, newname) 重命名文件

os.walk() 生成目录树下的所有文件名

os.chdir('dirname') 改变目录

os.mkdir/makedirs('dirname')创建目录/多层目录

os.rmdir/removedirs('dirname') 删除目录/多层目录

os.listdir('dirname') 列出指定目录的文件

os.getcwd() 取得当前工作目录

os.chmod() 改变目录权限

os.path.basename(‘path/filename’) 去掉目录路径，返回文件名

os.path.dirname(‘path/filename’) 去掉文件名，返回目录路径

os.path.join(path1[,path2[,...]]) 将分离的各部分组合成一个路径名

os.path.split('path') 返回( dirname(), basename())元组

os.path.splitext() 返回 (filename, extension) 元组

os.path.getatime\ctime\mtime 分别返回最近访问、创建、修改时间

os.path.getsize() 返回文件大小

os.path.exists() 是否存在

os.path.isabs() 是否为绝对路径

os.path.isdir() 是否为目录

os.path.isfile() 是否为文件
"""
