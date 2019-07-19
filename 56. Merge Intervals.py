class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        for pos, interval in enumerate(intervals):
            if res == []:
                res.append(interval)
            else:
                if interval[0]<=res[-1][1]:
                    res[-1][:] = [res[-1][0]]+[max(res[-1][1],interval[1] )]
                else:
                    res.append(interval)
        return res
        
