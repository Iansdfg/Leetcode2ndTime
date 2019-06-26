class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, summ = float('-inf'), 0
        for num in nums:
            summ = max(num, num+summ)
            res = max(res, summ)
        return res
        
