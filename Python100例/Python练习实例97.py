'''
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，
直到输入一个 # 为止。

程序分析：无。
'''
if __name__ == '__main__':
    from sys import stdout
    filename = input('输入文件名：\n')
    fp = open("C:/" + filename,'w')
    ch = input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('输入字符串:\n')
    fp.close()



