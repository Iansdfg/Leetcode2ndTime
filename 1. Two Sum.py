class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for pos, val in enumerate(nums):
            if val not in dic:
                dic[target-val] = pos
            else:
                return [dic[val], pos]
