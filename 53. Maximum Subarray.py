class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, left, right):
        if left==right:
            return nums[left]
        mid = (left+right)//2
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid+1, right)
        cross_sum = self.cross(nums, left, right, mid)
        return max(left_sum, right_sum, cross_sum)
        
    def cross(self, nums, left, right, mid):
        if left == right:
            return nums[left]
        
        right_sum= 0
        right_curr= float("-inf")
        for i in range(mid+1, right+1):
            right_sum += nums[i]
            right_curr = max(right_sum, right_curr)
            
        left_sum= 0
        left_curr= float("-inf")
        for i in range(mid, left-1, -1):
            left_sum += nums[i]
            left_curr = max(left_sum, left_curr)
        
        return left_curr+right_curr
            
