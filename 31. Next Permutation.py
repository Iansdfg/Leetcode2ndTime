class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j]>nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        nums[i+1:] = reversed(nums[i+1:])
                        return 
        nums[:] = reversed(nums[:])
        return 

            
            
        
