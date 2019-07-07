class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        sortest_dis = float('inf')
        for pos,num in enumerate(nums):
            l,r = pos+1,len(nums)-1
            while l<r:
                summ = nums[pos]+nums[l]+nums[r]
                if summ == target:return target
                if summ>target:
                    r-=1
                elif summ<target:
                    l+=1
                if abs(summ-target)<sortest_dis:
                    sortest_dis = abs(summ-target)
                    res = summ
        return res
                    
        
