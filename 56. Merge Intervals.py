class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x:x[0])
        res=[]
        for pos, ele in enumerate(intervals):
            if res == []:
                res.append(ele)
            else:
                if ele[0]<=res[-1][1]:
                    res[-1][:] = [res[-1][0]]+[max(ele[1],res[-1][1])]
                else:
                    res.append(ele)
        return res
            
            
