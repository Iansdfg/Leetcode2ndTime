class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle =='':
            return 0
        len_needle = len(needle)
        for pos in range(len(haystack)):
            if len(needle)+pos>len(haystack):break
            if haystack[pos:pos+len_needle] == needle:
                return pos
        return -1
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dic = {}
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                summ = nums[i]+nums[j]
                if summ not in dic:    
                    dic[summ] = [(i,j)]
                else:
                    dic[summ].append((i,j))
        print(dic)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                val = target - (nums[i]+nums[j])
                if val in dic:
                    for combo in dic[val]:
                        if combo[1]<i:
                            res.add((nums[combo[0]],nums[combo[1]],nums[i],nums[j]))
        return list([i for i in res])
                    
        
