#random 随机数
import random

print("random()的用法和结果如下")
#random() 获取0-1之间的随机小数
#格式：random.random()
#返回值：0-1之间的随机小数
ra = int(random.random()*100)
print(ra)
print("choice()的用法和结果如下")
#choice() 随机返回序列中的某个值
#格式：random.choice(序列)
l =[str(i)+'haha' for i in range(10)]
print(l)
rst = random.choice(l)
print(rst)
print("shuffle()的用法和结果如下")
#shuffle() 随机打乱列表
#格式：shuffle（列表）
#返回值：打乱之后的列表
l1 = [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)
print("randint()的用法和结果如下")
#格式：randint(a,b)
#返回值：随机返回一个a-b之间的随机整数，包括a和b
x = random.randint(1,2)
print(x)







