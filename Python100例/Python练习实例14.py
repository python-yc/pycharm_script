"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""
#coding:utf-8


# def reduceNum(n):
#     print ('{} = '.format(n),)
#     if not isinstance(n, int) or n <= 0 :
#         print ('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1] :
#         print ('{}'.format(n))
#     while n not in [1]:
#         for index in range(2,n+1):
#             if n % index == 0:
#                 n /= index
#                 if n == 1:
#                     print(index)
#                     break
#                 else:
#                     print(index, '*', end='')
#         break
#
#
# reduceNum(90)


#方法 1
# def reduceNumber(n):
#     k = 2
#     if not isinstance(n, int) or n < 2:
#         print("Please input a int number")
#         exit(0)
#     else:
#         print('{} = '.format(n), end='')
#         while k <= n:
#             if n == k:
#                 print(n)
#                 break
#             elif n % k == 0:
#                 print(k,'* ',end='')
#                 n = int(n/k)
#             else:
#                 k += 1
#
# reduceNumber(90)
# reduceNumber(10)

#方法 2

def recuceNum(n):
    print('{0} = '.format(n),end='')
    if not isinstance(n,int) or n <= 0:
        print('Please input a correct number!')
        exit(0)
    elif n in [1]:
        print('{0}'.format(n))
    while n not in [1]:
        for index in range(2,n+1):
            if n % index ==0:
                #注意在python中，如果两个数相除默认为float型，所以要想为整数，
                #一定要加int转换符
                n = int(n/index)
                if n ==1:
                    print(index)
                else:
                    print('{0} * '.format(index),end='')
                break

recuceNum(90)
recuceNum(100)

x = 4/2
y = int(6)/int(2)
print(x,'---',y)


