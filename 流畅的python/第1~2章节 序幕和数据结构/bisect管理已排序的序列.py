# -*- coding: utf-8 -*-

"""
bisect模块包含两个主要函数，bisect和insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素

bisect(haystack,needle)在haystack（干草垛）里搜索needle（针）的位置，该位置满足的条件是，
把needle插入这个位置之后，haystack还能保持升序。也就是在说这个函数返回的位置前面的值，都小于
或等于needle的值。其中haystack必须是一个有序的序列。你可以先用bisect(haystack,needle)查
找位置index，再用haystack.insert(index,needle)来插入新值。但你也可用insort来一步到位，
并且后者的速度更快一些
"""
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

row_fmt = '{0:2d} @ {1:2d}    {2} {0:<2d}'


# print(*reversed(NEEDLES))
# print(reversed(NEEDLES))

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(row_fmt.format(needle, position, offset))


if __name__ == '__main__':
    print(sys.argv)
    print(sys.argv[-1])
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    # print(HAYSTACK)

"""
bisect_left:将被插入的数据放在相等元素的前面；
bisect_right:将被插入的数据放在相等元素的后面；
对于相同的数无区别，但是对于相等有要求的就有区别，如果1 和1.0
# python bisect_demo.py left
"""


# 根据一个分数，找到它所对应的成绩
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)       # bisect = bisect_right
    # i = bisect.bisect_right(breakpoints, score)
    return grades[i]


result = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

print(result)
