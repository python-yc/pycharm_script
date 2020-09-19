"""
题目：请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，
则判断用情况语句或if语句判断第二个字母。
"""
letter = input("please input the first letter:\n")
if letter == 'M':
    print('Monday')
elif letter == 'T':
    letter = input("please input the Second letter")
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('data err')
elif letter == 'W':
    print('Wesdenday')
elif letter == 'F':
    print("Friday")
elif letter == 'S':
    letter = input('please input the Second letter')
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('data err')
else:
    print('data err')

