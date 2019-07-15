class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.findlower(nums, target)
        right = self.findhigher(nums, target)
        if left == right:
            return [-1,-1]
        return [left,right-1]
    
    def findlower(self, nums, target):
        l,r = 0, len(nums)
        while l<r:
            m = (l+r)//2
            if nums[m]<target:
                l = m +1
            else:
                r = m
        return l
    
    def findhigher(self, nums, target):
        l,r = 0, len(nums)
        while l<r:
            m = (l+r)//2
            if nums[m]<=target:
                l = m +1
            else:
                r = m
        return l
                
                
