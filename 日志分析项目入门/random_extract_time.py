import random
import datetime

def source():
    while True:
        yield datetime.datetime.now(), random.randint(1, 100)

## 方法一取3个数据
# src = source()
# i = 1
# for x in src:
#     print(x)
#     i += 1
#     if i>3:
#         break

## 方法二取3个数据
# src = source()
# i = 0
# for _ in range(3):
#     lst = []
#     lst.append(next(src))
#     lst.append(next(src))
#     lst.append(next(src))

## 方法三取3个数据
src = source()
i = 0
lst = []
lst.append(next(src))
lst.append(next(src))
lst.append(next(src))
print(lst)
# print(sum(lst) // len(lst))
