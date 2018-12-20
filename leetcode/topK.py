# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    算法描述：
        如何在10亿个数中找出前1000大的数
'''


def topK1(s, k):
    """
        计算S中第K大的数(个人实现)
        算法说明:
            维护一个K个无重复字符的有序(从大到小)列表或集合 KS，
            遍历S
                比较与KS中最小的元素(最后一个)，
                如果小于, 直接过滤，
                如果大于插入KS，
                对KS排序， 并删除KS中最小的元素
            遍历结束
            KS即为答案
        算法缺陷:
            每次需要对整个KS排序， 可以优化为小顶堆， 做少量排序
    :param s:
    :param k:
    :return:
    """
    # kd 前K大个数的列表
    ks = []
    for v in s:
        if v in set(ks):
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

print topK1(o, 4)

# output:
#   [10, 8, 7]

