class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return 0
        s = s.split(' ')
        for ele in s[::-1]:
            if ele != '':
                return len(ele)
        return 0
