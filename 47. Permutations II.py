class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        visited = [0]*len(nums)
        self.findPerm(nums, 0, [], res, visited)
        return res
    
    def findPerm(self, nums, depth, path, res, visited):         
        if len(path) == len(nums):
            res.append(path)
            return 
        for i in range(len(nums)):
            if visited[i] == 1:
                continue
            if i>0 and nums[i] == nums[i-1] and visited[i-1] == 0:
                continue 
            visited[i] = 1
            self.findPerm(nums, i, path+[nums[i]], res, visited)
            visited[i] = 0
            
        
        
