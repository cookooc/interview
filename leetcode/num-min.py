# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    算法描述:
       给定一个数 长度不限 可能很长也可能很短, 要求删除其中K个数, 使其组成新的数 是所有可能的新数中的最小值
       注:  每个位置上的数字只能向右移动 数字的相对位置不变
       例如:   13456 删除6 组成1345   最小
              172538 删除7 组成12538 最小
                     删除7 5 组成 1238 最小
    算法之死记硬背:
       规律是从左往右遍历 如果一个数的右边的数小于左边 则可以删除该数得到的值比其他数小
'''


def min_number(number, k):
    ks = []
    str_number = str(number)
    pre = str_number[0]
    i = 1
    while i < len(str_number):
        cur = str_number[i]
        if cur < pre:
            k -= 1
            ks.append(pre)
        i += 1
        pre = cur
    kks = []
    for s in str_number:
        kks.append(s)
        kks = sorted(kks)
        if len(kks) > k:
            kks.pop(0)
    return ks + kks


num = 172538
print min_number(num, 1)
print min_number(num, 3)
