class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []
        for word in strs:
            sortedword = ''.join(sorted(word))
            if sortedword not in dic:
                dic[sortedword] = [word]
            else:
                dic[sortedword] += [word]
        res = []
        for value in dic.values():
            res.append(value)
        return res
                
            
        
