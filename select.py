# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    选择排序
    算法之死记硬背:
       1. 选择排序在每次的比较中将一个无序的列表分为两部分： 一部分是有序， 一部分无序
       2. 每次循环指针对无序的列表选出最大或最小的元素 然后放置在该无序列表的首位
'''


def select(s):
    """

    :param s:
    :return:
    """
    for i in xrange(len(s)):
        preindex = i
        for j in xrange(i+1, len(s)):
            if s[i] > s[j]:
                i = j
        s[preindex], s[i] = s[i], s[preindex]
    return s


o = [5, 5, 4, 5, 44, 38, 27, 49, 26, 46, 19, 47, 48]
ss = select(o)
print ss
