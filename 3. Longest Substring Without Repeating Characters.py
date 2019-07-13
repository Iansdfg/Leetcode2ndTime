class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = dict()
        start,res = 0,0 
        for pos, value in enumerate(s):
            if value in chars:
                start = max(start, chars[value]+1)
            chars[value] = pos
            res = max(res, pos-start +1)
        return res
