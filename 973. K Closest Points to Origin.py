# class Solution(object):
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         points.sort(key = lambda p:p[0]**2+p[1]**2)
#         return points[:K]    
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dis = []
        for p in points:
            d = math.sqrt(p[0] ** 2 + p[1] ** 2)
            dis.append((d, p))
        heapq.heapify(dis)
        # print(dis)
        return [d[1] for d in heapq.nsmallest(K, dis)]
        
