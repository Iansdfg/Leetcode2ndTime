class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        if target>nums[-1]:return len(nums)
        l,r = 0, len(nums)
        while l<=r:
            m = (r+l)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m -1
        return l

        
