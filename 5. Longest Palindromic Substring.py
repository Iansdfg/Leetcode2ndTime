class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in range(len(s)):
            pal1 = self.palindrome(s,i,i)
            if len(pal1) > len(ans): ans = pal1
            pal2 = self.palindrome(s,i, i + 1)
            if len(pal2) > len(ans): ans = pal2
        return ans
        
    def palindrome(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
        
        
