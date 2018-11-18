# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    插入排序
'''


def insertion(s):
    """

    :param s:
    :return:
    """
    for i in xrange(1, len(s)):
        # 有序序列的最大元素的下标
        sli = i - 1
        current = s[i]
        while sli >= 0 and s[sli] > current:
            s[sli+1] = s[sli]
            sli -= 1
        s[sli+1] = current
    return s


o = [1, 5, 3, 4, 2]
print insertion(o)
