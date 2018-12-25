# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

例子:
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
"""


def FindMedianSortedArrays(nums1, nums2):
    """
        arr=[]
        l1=len(nums1)
        l2=len(nums2)
        i,j=0,0
        odd = (l1+l2)%2 >0
        num=int(sum([l1,l2])/2)
        while i<l1 and j<l2:
            if nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i=i+1
            elif nums1[i]==nums2[j]:
                arr.extend([nums1[i],nums2[j]])
                i+=1
                j+=1
            else:
                arr.append(nums2[j])
                j+=1
            if len(arr)>num+1 :
                break;
        if len(arr)<=num+1:
            if i<l1:
                arr.extend(nums1[i:])
            else:
                arr.extend(nums2[j:])
        if odd:
            return arr[num]
        else:
            return (arr[num-1]+arr[num])/2.0
    :param nums1:
    :param nums2:
    :return:
    """
    length = len(nums1) + len(nums2)
    if length % 2 == 0:
        first, second = length / 2 - 1, length / 2
    else:
        first = second = length / 2
    i, j = 0, 0
    nums3 = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1
        if len(nums3) > second + 1:
            break
    if len(nums3) < second + 1:
        if i == len(nums1):
            nums3.extend(nums2[j:])
        if j == len(nums2):
            nums3.extend(nums1[i:])
    return float(nums3[first] + nums3[second]) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2, 4]
    print FindMedianSortedArrays(nums1, nums2)
