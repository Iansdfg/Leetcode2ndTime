class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        summ = 0
        for num in nums:
            summ = max(summ + num, num)
            res = max(res, summ)
        return res
        
