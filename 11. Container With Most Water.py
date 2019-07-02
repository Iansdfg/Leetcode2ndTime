class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        maxx = 0
        while l<r:
            low = min(height[r],height[l])
            maxx = max(maxx, (r-l)*low)
            if height[l]<=height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
        return maxx
            
        
