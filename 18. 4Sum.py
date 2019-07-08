class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1
                while l<r:
                    if l>j+1 and r<len(nums)-1 and nums[l] == nums[l-1] and nums[r] == nums[r+1]:
                        r-=1
                        l+=1
                        continue
                    summ = nums[i]+nums[j]+nums[l]+nums[r]
                    if summ == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        r-=1
                        l+=1
                    elif summ<target:
                        l+=1
                    else:
                        r-=1
        return res
                
        
