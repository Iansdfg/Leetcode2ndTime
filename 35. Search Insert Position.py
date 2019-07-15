class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        if target>nums[-1]:return len(nums)
        for pos, val in enumerate(nums):
            if val == target or val > target:
                return pos

        
