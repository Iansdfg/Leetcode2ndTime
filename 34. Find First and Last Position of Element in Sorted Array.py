class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lower(nums, target)
        right = self.higer(nums, target)
        if right == left:
            return [-1, -1]
        return [left, right - 1]
    
    def lower(self, nums, target):
        l,r = 0,len(nums)
        while l<r:
            m = (r+l)//2
            if nums[m]<target:
                l = m+1
            else:
                r = m
        return l
    
    def higer(self, nums, target):
        l,r = 0,len(nums)
        while l<r:
            m = (r+l)//2
            if nums[m]<=target:
                l = m+1
            else:
                r = m
        return l

