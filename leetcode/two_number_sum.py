# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
给定 nums = [11, 7, 2, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution(object):

    def TwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targets = {}
        for i, num in enumerate(nums):
            if target - num in targets:
                return targets[target - num], i
            targets[num] = i
        return targets


if __name__ == '__main__':
    print Solution().TwoSum([3, 2, 4], 6)
    print Solution().TwoSum([2, 3, 4], 6)
    print Solution().TwoSum([-5, -3, -2, -1], -8)
    print Solution().TwoSum([-10, -1, -18, -19], -19)
    print Solution().TwoSum([-1, -2, -3, -4, -5], -8)
