class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 1
        while fast< len(nums):
            if nums[slow] == nums[fast]:
                fast+=1
            else:
                slow+=1
                nums[slow] = nums[fast]
        return slow+1
                
        
