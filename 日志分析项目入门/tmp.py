from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# def human(size: int):
#     units = ['', 'K', 'M', 'G', 'T', 'P']  # " KMGTP"
#     depth = 0
#
#     while size >= 1000:
#         size = size // 1000
#         depth += 1
#
#     return "{}{}".format(size, units[depth])
#
# print(human(900))
# print(human(9005))
# print(human(90000))
# #TypeError: unorderable types: str() >= int()
# # print(human("90"))
#
# lists = [
#     1, 2, 3,
#     [4, 5, [6, 7], 8],
#     [[[9, 10], 11]],
#     [[]],
#     12,
# ]
#
# def flatten(items):
#     for item in items:
#         if isinstance(item, (list, tuple)):
#             yield from flatten(item)
#         else:
#             yield item
#
# print(flatten(lists))
# b = flatten(lists)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# def helloYield():
#     print('exe 1')
#     yield '1 be exed'
#     print('exe 2')
#     yield '2 be exed'
#
# gen=helloYield()
# print(next(gen))
# print(gen.__next__())

a = "hello"
b = 4
if isinstance(a, str):
    print("a is str")
if isinstance(b, int):
    print("yes")
else:
    print("no")


