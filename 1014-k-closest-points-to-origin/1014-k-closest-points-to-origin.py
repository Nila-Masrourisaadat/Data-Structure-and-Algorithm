class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # #O(nlogn)
        # distance=[]
        # for i,(x,y) in enumerate(points):
        #     distance.append((x**2+y**2,i))
        # #sort based on the first element of the tuples in the array distance
        # distance.sort(key=lambda x:x[0] )
        # return [points[dis[1]] for dis in distance[:k]]

        #o(nlogn)but without sort function
        distance=[]
        res=[]
        for i,(x,y) in enumerate(points):
            heapq.heappush(distance,(x**2+y**2,i))
        for i in range(k):
            dis=heapq.heappop(distance)[1]
            res.append(points[dis])
        return res