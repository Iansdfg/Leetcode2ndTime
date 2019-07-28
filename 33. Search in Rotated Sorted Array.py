class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:return m
            elif nums[m]>=nums[l]:
                if  nums[l]<=target<nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m]<=nums[r]:
                if  nums[m]<target<=nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
