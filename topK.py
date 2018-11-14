# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    算法描述：
        如何在10亿个数中找出前1000大的数
'''

"""
    个人实现
"""


def topK(s, k):
    """
        计算S中第K大的数
    :param s:
    :param k:
    :return:
    """
    # kd 前K大个数的列表
    ks = []
    for v in s:
        print ks
        if v in ks:
            continue
        else:
            if len(ks) < k:
                ks.append(v)
                ks = sorted(ks, reverse=True)
                continue
            else:
                if ks[-1] > v:
                    continue
                else:
                    ks.pop(-1)
                    ks.append(v)
                    ks = sorted(ks, reverse=True)

    return ks


o = [10, 10, 10, 6, 8, 8, 10, 5, 5, 7]

print topK(o, 4)

# [10, 8, 7]
