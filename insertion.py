# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    插入排序
    插入排序之死记硬背
    1. 需要额外的存储 用来存储排序后的结果
    2. 每次从原来列表中取出数据与有序的结果作比较
'''


def insertion(s):
    """

    :param s:
    :return:
    """
    ds = []
    for i in xrange(len(s)):
        skip = False
        for j in xrange(len(ds)):
            if s[i] < ds[j]:
                ds.insert(j, s[i])
                skip = True
                break
        if not skip:
            ds.append(s[i])
    return ds


o = [3, 5, 4, 5, 44, 38, 27, 49, 26, 46, 19, 47, 48]
# print insertion(o)

