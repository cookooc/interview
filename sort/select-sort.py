# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    选择排序
    算法之死记硬背:
       算法分两层循环, 
       外层循环代表内层循环最小值的存放位置
       内层循环负责选出最小值并记录最小值的索引位置
       内层循环结束将最小值与外层循环标记的存放位置交换
'''


def select(s):
    """

    :param s:
    :return:
    """
    for i in xrange(len(s)):
        minindex = i
        for j in xrange(i+1, len(s)):
            if s[minindex] > s[j]:
                minindex = j
        s[i], s[minindex] = s[minindex], s[i]
        print i, s
    return s


o = [9, 8, 7, 6, 5, 4, 3, 2, 1]
ss = select(o)
print ss
