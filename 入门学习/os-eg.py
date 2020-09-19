#OS 模块
import os
print("getcwd的用法结果如下")
#getcwd()获取当前路径
#格式：os.getcwd()
#返回值：当前目录的字符串
mydir = os.getcwd()
print(mydir)
print("chdir的用法结果如下")
#chdir()改变当前的工作目录 --change director
#格式：os.chdir(路径)
#返回值：无
os.chdir('C:')
mydir = os.getcwd()
print(mydir)
####在当前路径创建了一个z.txt文档
open('a.txt','w')
print("listdir的用法结果如下")
#listdir() 获取一个目录中所有子目录和文件的名称列表
#不会递归列出，即只列出当前的
#格式：os.listdir(路径)
ld = os.listdir('C:')
print(ld)
print("makedirs的用法结果如下")
#makedirs()递归创建文件夹
#格式：os.makedir(递归路径)
#返回值：None，创建了目录
if os.path.exists('c:/a/b/h'):
    print('创建的目录已存在')
else:
    os.makedirs('c:/a/b/h')
    print("sucess!")
print("当前路径为：",os.getcwd())
print("system的用法结果如下")

#system()运行系统shell命令
#格式：os.system(系统命令)
#返回值：命令结果
#dir是列出当前文件和文件夹的系统命令
rst = os.system('dir')
print(rst)
print("getenv的用法结果如下")
#getenv()获取指定系统的环境变量
#相应的还有putenv
#格式：os.get.env('环境变量名')
#返回值：指定环境变量对应的值
rst = os.getenv("PATH")
print(rst)
print('exit的例子结不执行了')
#exit()退出当前程序
#格式：exit()
print('pardir,curdir等值部分的例子就不执行了')
'''
#################值部分########

os.curdir,当前目录 --current dir
os.pardir,父亲目录 --parent dir
os.sep，当前系统的路径分隔符
os.linesep，当前系统的换行符
    - windows:“\n\t”
    - unix,linux:“\n”
os.name，当前系统名称
    - windows:“nt”
    - unix,linux:“posix”
'''
print(os.pardir)
print(os.curdir)
print("os.sep: "+os.sep)
print("------")
print(os.linesep)
print("------")
print(os.name)


