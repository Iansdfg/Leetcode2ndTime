class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.findPrem(nums, 0, [], res)
        return res
    
    def findPrem(self, nums, depth, path, res):
        if len(path) == len(nums):
            res.append(path)
            return 
        for i in range(len(nums)):
            if nums[i] not in path:
                self.findPrem(nums, i, path+[nums[i]], res)
    
        
