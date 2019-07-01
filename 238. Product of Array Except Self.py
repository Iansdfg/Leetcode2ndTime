# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         lr = [0]*len(nums)
#         tmp = 1
#         for i in range(len(nums)):
#             lr[i] = tmp
#             tmp *= nums[i]
#         tmp = 1
#         rl = [0]*len(nums)
#         for i in range(len(nums)-1,-1,-1):
#             rl[i] = tmp
#             tmp *= nums[i]
#         res = []
#         for i in range(len(nums)):
#             res.append(lr[i]*rl[i])
#         return res
                 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        tmp = 1
        for i in range(len(res)):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= tmp
            tmp *= nums[i]
        return res
            
        
        
        
