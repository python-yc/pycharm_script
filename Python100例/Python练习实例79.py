'''
题目：字符串排序。

程序分析：无。
'''
if __name__ == '__main__':
    str1 = input('input the first character\n')
    str2 = input('input the second character\n')
    str3 = input('input the third character\n')

    if str1 > str2 : str1,str2 = str2,str1
    if str1 > str3 : str1,str3 = str3,str1
    if str2 > str3 : str2,str3 = str3,str2

    print('after being sorted')
    print(str1,'\t',str2,'\t',str3)






