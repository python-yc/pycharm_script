from pathlib import Path
import argparse

def showdir(path:str='.'):
    p = Path(path)
    for file in p.iterdir():
        print(file.name)

# ls [path] [-l] [-a] [-h]
# 此处add_help为True时会与parser.add_argument('-h',action='store_true')中的-h冲突，所以为False
parser = argparse.ArgumentParser(prog='ls', add_help=False, description='list all files')  # 构造解析器
parser.add_argument('path',nargs='?',default='.',help='path help')  # 位置参数
# parser.add_argument('-l',action='store_true')
parser.add_argument('-h',action='store_true')   #添加了这一项后，会有参数冲突，此时需要将parser中的add_help改为False
parser.add_argument('-l',action='store_true')
parser.add_argument('-a', '--all',action='store_true')


if __name__ == '__main__':
    showdir('C:/a')
    #parser.add_argument()
    args = parser.parse_args(('/etc','-lah'))  #此时注意添加减少alh参数时输出
    parser.print_help()

    print("args=",args)
    print(args.path,args.l,args.h,args.all)
#  python parse_argv.py 1 2

