# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    冒泡排序算法
    算法之死记硬背:
       冒泡排序分两层循环
       外层循环 内层循环每次只能比较出一个结果 因此 外层循环有N（元素个数）个内层循环
       内层循环 最大值或最小值在比较的过程中存在调换(如果比较条件为正)
    冒泡排序与选择排序:
       相同点:
         冒泡排序和选择排序都分两层循环
         内层循环都是每次选出一个最小值
         外层循环控制内层循环需要进行的次数
       不同点:
         冒泡排序的内层循环 每次相邻的两个元素比较 不满足条件 调换值
         选择排序的内层循环 每次选出的最小值与每个元素比较 不满足条件 调换最小值的下标 内层循环结束 调换值
    总结:
       选择排序相对冒泡排序减少了交换次数
'''


def bubble(s):
    for i in xrange(len(s)):
        for j in xrange(len(s)-i-1):
            if s[j] > s[j+1]:
                s[j+1], s[j] = s[j], s[j+1]
    return s


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


o = [3, 2, 4, 5, 44, 38, 27, 49, 26, 46, 19, 47, 48]
ss = bubble(o)
print ss
