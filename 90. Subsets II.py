class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.findSub(nums,0, [], res)
        return res
    
    def findSub(self,nums, depth, path, res ):
        res.append(path)
        for i in range(depth, len(nums)):
            if i>depth and nums[i]==nums[i-1]:
                continue
            self.findSub(nums, i+1, path+[nums[i]], res)
        
