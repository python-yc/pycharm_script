"""
题目：文本颜色设置。

程序分析：无。
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARING + "警告的颜色字体？" + bcolors.ENDC)
print(bcolors.OKBLUE + "OK颜色字体？" )
print(bcolors.HEADER + "HEADER的颜色字体？" )
print(bcolors.FAIL + "失败的颜色字体？")
print(bcolors.UNDERLINE + "下划线的颜色字体？")





