from pathlib import Path
import argparse
import datetime

# def convert_mode(mode:int):
#     modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']    #list('rwxrwxrwx')
#     modestr = bin(mode)[-9:]    #'110110100'
#     ret = ""
#     for i,c in enumerate(modestr):
#         if c == '1':
#             ret += modelist[i]
#         else:
#             ret += '-'
#     return ret
#
# # d - s p l c b
# def convert_type(files:Path):
#     if files.is_symlink():
#         ret = 'l'
#     elif files.is_fifo():
#         ret = 'p'
#     elif files.is_socket():
#         ret = 's'
#     else:
#         ret = '-'
#     return ret


# 900 2000=2K

def listdir(path='.', all=False, detail=False, human=False):
    def _get_human(size:int):
        units = [ '', 'K', 'M', 'G', 'T', 'P' ]  #" KMGTP"
        depth = 0

        while size >= 1000:
            size = size //1000
            depth += 1

        return "{}{}".format(size,units[depth])



    def _showdir(path='.', all=False, detail=False,human=False):
        p = Path(path)
        for file in p.iterdir():
            if not all and str(file.name).startswith('.'): # .开头不打印 --all
                continue

            # -l
            if detail:
                st = file.stat()
                #  -rw-rw-r--
                h = st.st_size
                if _get_human:
                    h = _get_human(st.st_size)
                yield (st.st_mode, st.st_nlink, st.st_uid, st.st_gid, str(h),
                      st.st_atime, file.name)
            else:
                yield (file.name,)

    #yield form是一个一个返回，直接yield是一次返回，与return类似
    yield from sorted(_showdir(args.path, args.all, args.l, args.h), key=lambda x: x[len(x)-1])

# ls [path] [-l] [-a] [-h]
parser = argparse.ArgumentParser(prog='ls', add_help=False, description='list all files')  # 构造解析器
parser.add_argument('path',nargs='?',default='.',help='path help')  # 位置参数
parser.add_argument('-h',action='store_true')   #添加了这一项后，会有参数冲突，此时需要将parser中的add_help改为False
parser.add_argument('-l',action='store_true')
parser.add_argument('-a', '--all',action='store_true')


if __name__ == '__main__':
    args = parser.parse_args(('C:/a','-l'))  #此时注意添加减少alh参数时输出
    parser.print_help()
    print("args=",args)
    # print(args.path,args.l,args.h,args.all)

    for file in listdir(args.path, args.all, args.l, args.h):
        print(file)


