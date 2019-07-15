class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res =[]
        for ele in strs:
            sortedstr = "".join(sorted(ele))
            dic[sortedstr] = [ele] if sortedstr not in dic else dic[sortedstr]+[ele]
        for val in dic.values():
            res.append(val)
        return res
            
        
