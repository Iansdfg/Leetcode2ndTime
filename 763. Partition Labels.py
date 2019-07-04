class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_appear = {}
        last_pos, anchor = 0, 0
        res = []
        for pos, char in enumerate(S):
            last_appear[char] = pos 
        for pos, char in enumerate(S):
            last_pos = max(last_pos, last_appear[char])
            if pos == last_pos:
                res.append(pos-anchor+1)
                anchor = pos+1
        return res
                
            
