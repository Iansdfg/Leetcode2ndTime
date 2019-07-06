# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         strs.sort()
#         if len(strs)==0:return ''
#         for pos, char in enumerate(strs[0]):
#             for ele in strs:
#                 if pos>=len(ele) or ele[pos]!=char:
#                     return strs[0][:pos]
#         return strs[0]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:return ''
        res =''
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
