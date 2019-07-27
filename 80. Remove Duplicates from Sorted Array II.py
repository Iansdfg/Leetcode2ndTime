class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:return len(nums)
        slow, fast = 1,2
        while fast<len(nums):
            if nums[fast]==nums[slow]==nums[slow-1]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow+1
