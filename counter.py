# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    计数排序 
    计数排序之死记硬背:
    1. 计数排序 适用于 列表中的数据具备一定的范围
    2. 计数排序 主要利用字典的特点， 用数字作为key list作为value, 重复数字记录到list中
'''

from collections import defaultdict, OrderedDict


def counter(s):
    """
        计数排序
    :param s:
    :return:
    """
    c = defaultdict(list)
    for v in s:
        c[v].append(v)
    keys = sorted(c)
    s_c = OrderedDict()
    for k in keys:
        s_c[k] = c[k]
    d_s = []
    for k, v in s_c.iteritems():
        for i in v:
            d_s.append(i)
    return d_s


o = [3, 5, 4, 5, 44, 38, 27, 49, 26, 46, 19, 47, 48]
print counter(o)
