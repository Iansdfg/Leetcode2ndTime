
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.sub(nums, 0, [], res)
        return res
    
    def sub(self, nums, depth, path, res):
        res.append(path)
        for i in range(depth,len(nums)):
            self.sub(nums, i+1, path+[nums[i]], res)
