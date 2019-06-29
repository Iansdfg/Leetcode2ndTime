class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or not intervals[0]:return 0
        stamps = []
        for interval in intervals:
            stamps.append([interval[0], True])
            stamps.append([interval[1], False])
        stamps.sort()
        n, maxx = 0, 0
        for stamp in stamps:
            if stamp[1]:
                n+=1
            else:
                n-=1
            maxx = max(maxx, n)
        return maxx
            
