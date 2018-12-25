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


def is_recycle_string(s, i, j, longest):
    """
        judge the string is recycle
    :param s:
    :param i:
    :param j:
    :param longest:
    :return:
    """
    if s[i] == s[j]:
        if longest:
            space = longest[1] - longest[0]
            if space < 3:
                return True
            if space >= 3 and longest[0] == i-1 and longest[1] == (j - 1):
                return True
        else:
            return True
    return False


def longest_recycle_string(string):
    """

    :param string:
    :return: start_index, end_index
    """
    longest = {}
    for i in xrange(len(string)):
        for j in xrange(i, len(string)):
            if i == j:
                longest[(i, j)] = 1
            elif j - i == 1 and string[j] == string[i]:
                longest[(i, j)] = 1
            else:
                if string[j] == string[i] and (i-1, j-1) in longest:
                    longest[(i, j)] = 1

    return string[longest[0]: longest[1]+1]


if __name__ == '__main__':

    print longest_recycle_string("abcda")
    print longest_recycle_string("caba")
    print longest_recycle_string('cbbd')
    """
    output: (1, 2)
    """
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
    print longest_recycle_string('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')