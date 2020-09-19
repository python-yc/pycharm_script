'''
题目：写一个函数，求一个字符串的长度，
在main函数中输入字符串，并输出其长度。

程序分析：无。
'''
def strLength(str):
    return len(str)

if __name__ == '__main__':
    str = input('please input')
    x = strLength(str)
    print('The length of character you input is %d' %x)