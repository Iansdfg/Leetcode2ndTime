class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[count]!=nums[i]:
                nums[count+1],nums[i] = nums[i],nums[count+1]
                count+=1
        return count+1
