class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        if len(strs)==0:return ''
        for pos, char in enumerate(strs[0]):
            for ele in strs:
                if pos>=len(ele) or ele[pos]!=char:
                    return strs[0][:pos]
        return strs[0]
