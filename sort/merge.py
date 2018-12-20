# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    归并排序之死记硬背:
    1. 将待排列表 分为两部分, 针对每一部分再进行归并排序, 当列表长度小于 2 返回
    2. 返回结果的合并, 采用依次比较, 注意考虑列表比较完之后 还有元素存在, 要将剩余的元素合并到结果
              
'''


def merge(s):
    if len(s) < 2:
        return s
    left = merge(s[:len(s)/2])
    right = merge(s[len(s)/2:])
    rr, l_i, r_i = [], 0, 0
    while l_i < len(left) and r_i < len(right):
        if left[l_i] < right[r_i]:
            rr.append(left[l_i])
            l_i += 1
        else:
            rr.append(right[r_i])
            r_i += 1
    if l_i < len(left):
        rr.extend(left[l_i:])
    if r_i < len(right):
        rr.extend(right[r_i:])
    return rr


o = [7, 3, 8, 2, 6, 9, 5]
print merge(o)
