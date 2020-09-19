'''
题目：八进制转换为十进制

程序分析：无。
'''
if __name__ == '__main__':
    n = 0
    p = str(input('input a octal number:\n'))
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)




