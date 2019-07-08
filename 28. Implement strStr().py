class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack:
            return 0
        len_needle = len(needle)
        for pos in range(len(haystack)):
            if haystack[pos:pos+len_needle] == needle:
                return pos
        return -1
            
            
            
