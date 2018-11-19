# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    快速排序算法
       之死记硬背:
        1. 快速排序 首先选择一个基准数 将整个列表分为两部分  大于基准的列表和小于基准的列表
                   对于剩下的两部分再次采用递归调用
        2. 快速排序 需要额外的变量存储基准数的位置, 也即两部分的分界点
'''


def quick(s):
    """
        o = [7, 3, 4, 2, 6, 9, 5]
    """
    if len(s) < 2:
        return s
    k = s[0]
    # j 是k值要摆放的位置
    j = 0
    for i in xrange(1, len(s)):
        if s[i] <= k:
            s[i], s[j] = s[j], s[i]
            j += 1
    s[i], s[j] = s[j], s[i]
    left = quick(s[:j])
    right = quick(s[j:])
    left.extend(right)
    return left


o = [7, 3, 8, 2, 6, 9, 5]
#   [3, 7, 8, 2, 6, 9, 5] j = 1
#   [3, 2, 8, 7, 6, 9, 5] j = 2
#   [3, 2, 6, 7, 8, 9, 5] j = 3
#   [3, 2, 6, 5, 8, 9, 7] j = 4
#   [3, 2, 6, 5, 7, 9, 8] j = 4

print quick(o)
