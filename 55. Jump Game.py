class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = nums[0]
        for i in xrange(len(nums)):
            if reach<i: return False
            reach = max(reach, i + nums[i])
        return reach >= len(nums)-1
