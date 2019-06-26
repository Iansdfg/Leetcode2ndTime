# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res, summ = float('-inf'), 0
#         for num in nums:
#             summ = max(num, num+summ)
#             res = max(res, summ)
#         return res
        
class Solution(object):
    def cross_sum(self, nums, l, r, m):
        if l==r: return nums[l]
        
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(m,l-1,-1):
            curr_sum += nums[i]
            left_sum = max(curr_sum, left_sum)
        
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(m+1, r + 1):
            curr_sum += nums[i]
            right_sum = max(curr_sum, right_sum)
        return right_sum+left_sum
        
    def helper(self, nums, l, r):
        if l==r: return nums[l]
        m = (l+r)//2
        sumL = self.helper(nums, l, m)
        sumR = self.helper(nums, m+1, r)
        sumCro =self.cross_sum(nums, l, r, m)
        
        return max(sumL,sumR,sumCro )
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
        
