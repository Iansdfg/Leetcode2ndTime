class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        indx = dict()
        lastAppearPos = 0
        anchor = 0
        res = []
        for pos, value in enumerate(S):
            indx[value] = pos
        for pos, value in enumerate(S):
            lastAppearPos = max(lastAppearPos, indx[value])
            if pos == lastAppearPos:
                res.append(pos-anchor+1)
                anchor = pos+1
        return res
