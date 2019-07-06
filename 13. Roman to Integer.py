class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nums = [dic[c] for c in s]
        curr,prev = 0,0
        for num in nums:
            curr += num
            if prev<num:
                curr-=prev*2
            prev = num
        return curr
        
