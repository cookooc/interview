# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


"""
    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    说明:
    
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    示例:
    
    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    
    输出: [1,2,2,3,5,6]
    
"""
"""
    推理过程 
    题目隐含 nums2/nums1 的最大值如果小于 nums1/nums2 中的一个值, 那 nums2/nums1 中的所有都小于该值
    因此, 可以从 nums2/nums1 的最大值开始比较
"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i, j = m-1, n-1
    nums1.extend([0]*n)
    while i >= 0 or j >= 0:
        if i < 0:
            for p in xrange(j):
                nums1[p] = nums2[p]
            break
        if j < 0:
            break
        if nums1[i] > nums2[j]:
            nums1[j+i+1] = nums1[i]
            i -= 1
        else:
            nums1[j+i+1] = nums2[j]
            j -= 1
    return nums1


if __name__ == '__main__':
    n1 = [1, 2, 4, 5]
    n2 = [3, 5, 6]
    print merge(n1, 4, n2, 3)
