class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda point: self.fromOrigin(point))
        return points[:K]


    def fromOrigin(self, point):
        return (point[0]**2 + point[1]**2)**0.5
# class Solution(object):
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         dis = []
#         for p in points:
#             d = math.sqrt(p[0] ** 2 + p[1] ** 2)
#             dis.append((d, p))
#         heapq.heapify(dis)
#         # print(dis)
#         return [d[1] for d in heapq.nsmallest(K, dis)]
        
