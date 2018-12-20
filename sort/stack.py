# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


"""
    堆排序原理:
    从第一个非叶子节点开始, 选择每个堆中的最大或最小元素
    1. 第一个非叶子节点计算
            1         0
        2       3     2
    4      5           
"""


def stack(s):
    i = 0
    while len(s):
        s = adjust(s[i:])
        n = s.pop(0)
        print n,


def adjust(s):
    for i in xrange((len(s)) / 2 - 1, -1, -1):

        for j in xrange(i, len(s) / 2):
            if 2 * j + 1 < len(s) and s[j] > s[2 * j + 1]:
                s[j], s[2 * j + 1] = s[2 * j + 1], s[j]
            elif 2 * j + 2 < len(s) and s[j] > s[2 * j + 2]:
                s[j], s[2 * j + 2] = s[2 * j + 2], s[j]

    return s


stack([1, 3, 5, 2, 4, 7, 6])
