class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2-sum(nums)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for num in nums:
            if num in res:
                res.remove(num)
            else:
                res.append(num)
        return res[0]
        
