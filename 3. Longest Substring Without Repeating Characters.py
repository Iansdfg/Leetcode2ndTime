class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, res = 0, 0
        chars = dict()
        for r, value in enumerate(s):
            if value in chars:
                l = max(chars[value]+1, l)
            chars[value] = r
            res = max(res, r-l+1)
        return res
#         chars, res = set(), 0
#         l, r = 0, 0
#         while l<len(s) and r<len(s):
#             if s[r] in chars:
#                 if s[l] in chars:
#                     chars.remove(s[l])
#                 l+=1
#             else:
#                 chars.add(s[r])
#                 r+=1
#                 res = max(res, len(chars))
#         return res
            
        
