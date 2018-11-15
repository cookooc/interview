# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    冒泡排序算法
    算法之死记硬背:
       冒泡排序主要比较两个相邻的元素, 即 s[j] > s[j+1]
       每次比较的结果 如果为正, 调换两个相邻的元素.
'''


def bubble(s):
    for i in xrange(len(s)):
        for j in xrange(len(s)-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s


o = [3, 5, 4, 5, 44, 38, 27, 49, 26, 46, 19, 47, 48]
ss = bubble(o)
print ss
