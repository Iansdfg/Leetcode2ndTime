class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = nums[0]
        i = 1
        while i < len(nums) and reach >= i:
            reach = max(reach, i + nums[i])
            i += 1
        return reach >= (len(nums)-1)
