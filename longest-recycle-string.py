# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    求一个字符串的最长回环子串
    解释: 回环子串是一个字符串正读和反读是一样的
    例如:
        s = abacdb
        r = aba
    算法之死记硬背:
        1. 遍历每一个元素与其他元素相比, 判断是否相等, 相等继续判断之间的字符组合是否是回环子串
        2. 记录每次的回环子串的最后一个元素在原字串的索引位置, 
           那么下次循环直接从最后一个元素的下一个元素开始比较,
           因为中间的元素即使有回环子串也没有之前的长度长
        3. 每次遍历的过程中如果字符串的剩余子串的长度小于已经记录的最大字串长度 则直接结束
        
'''


def is_recycle_string(s):
    """
        judge the string is recycle
    :param s:
    :return:
    """
    length = len(s)
    for i in xrange(length/2):
        if s[i] != s[length - i - 1]:
            return False
    return True


def longest_recycle_string(string):
    """

    :param string:
    :return: start_index, end_index
    """
    count = 0
    longest = (0, 0)
    start = 0
    for i in xrange(len(string)):
        for j in xrange(start+1, len(string)):
            count += 1
            if is_recycle_string(string[i: j+1]):
                if (longest[1] - longest[0]) < (j - i):
                    longest = (i, j)
                start = j
        if not start:
            start = i
        if len(string[longest[0]: longest[1]+1]) >= (len(string) - i):
            break
    print count
    return longest


if __name__ == '__main__':

    print longest_recycle_string('cbbd')
    """
    output: (1, 2)
    """
    print longest_recycle_string('dbbd')
    """
    output: (0, 3)
    """
    print longest_recycle_string('abcdcba')
    """
    output: (0, 6)
    """
    print longest_recycle_string('abcdefedcba')
    """
    output: (0, 10)
    """
    print longest_recycle_string('aaabcdefedcbacc')
    """
    output: (2, 12)
    """