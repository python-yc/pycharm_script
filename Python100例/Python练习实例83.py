'''
题目：求0—7所能组成的奇数个数。

程序分析：

组成1位数是4个。

组成2位数是7*4个。

组成3位数是7*8*4个。

组成4位数是7*8*8*4个。

......
这个分析是根据排列组合得到
'''
# sum = 0
# for i in range(8):
#     for j in range(8):
#         for k in range(8):
#             for l in range(8):
#                 for m in range(8):
#                     for n in range(8):
#                         for o in range(8):
#                             for p in range(8):
#                                 s = int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p))
#                                 if s % 2 == 1:
#                                     sum += 1
# print(sum)

if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print (sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print ('sum = %d' % sum)

