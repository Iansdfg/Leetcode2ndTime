class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            even = self.palindrome(s, i, i+1)
            if len(even)>len(res):
                 res = even
            odd = self.palindrome(s, i, i)
            if len(odd)>len(res):
                 res = odd
        return res
        
        
        
    def palindrome(self, s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1: r]
        
