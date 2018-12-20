# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    桶排序
    算法之死记硬背:
       1. 桶排序类似计数排序, 但是桶排序多按照范围划分, 计数排序相当于范围只有一个元素
       2. 桶排序适用于数据结合的范围已知
'''


class Bucket(object):
    def __init__(self, start, end):
        """
            start <= bucket <= end
        :param start:
        :param end:
        """
        self.start = start
        self.end = end
        self.bucket = []

    def push(self, value):
        """
            桶内采用插入排序构建一个从小到大的列表
        :param value:
        :return:
        """
        self.bucket.append(value)
        i = len(self.bucket) - 1
        while self.bucket[i-1] > value:
            self.bucket[i] = self.bucket[i-1]
            i -= 1
        self.bucket[i] = value

    def __gt__(self, other):
        if isinstance(other, int):
            return self.start > other
        return self.start > other.end

    def __lt__(self, other):
        if isinstance(other, int):
            return self.end < other
        return self.end < other.start

    def __contains__(self, item):
        return self.start < item < self.end

    def __iter__(self):
        return iter(self.bucket)


def bucket(s):
    """
        桶排序
        假设  0 < s[i] < 10, 桶的数量 bs = 2
        其中:
            bs1: 0 < 5
            bs2: 5 < 10
    :param s:
    :return:
    """
    bs1 = Bucket(0, 5)
    bs2 = Bucket(5, 10)
    for v in s:
        if v in bs1:
            bs1.push(v)
        if v in bs2:
            bs2.push(v)
    ds = []
    for v in bs1:
        ds.append(v)
    for v in bs2:
        ds.append(v)
    return ds


o = [1, 1, 3, 2, 2, 5, 4, 6, 7, 7, 5, 4, 9, 8, 4, 1, 4, 6, 3]
print bucket(o)
