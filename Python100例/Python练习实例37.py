"""
题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，
选择一个最小的与第一个元素交换，下次类推，即用第二
个元素与后8个进行比较，并进行交换。
"""
if __name__ == '__main__':
    #方法一：冒泡排序
    N = 5
    print("请输入5个数字：")
    l = []
    for i in range(1,6):
        print("请输入第",str(i),"个数字:")
        l.append(int(input()))
    print(l)
    for k in range(4):
        for num in range(1,5):
            if l[num-1] > l[num]:
                l[num-1],l[num] = l[num],l[num-1]

    print(l)

    # 方法二：选择排序
    for i in range(4):
        min = i
        for j in range(i+1,5):
            if l[min] > l[j]:
                min = j
        l[i],l[min] = l[min],l[i]
    print(l)


