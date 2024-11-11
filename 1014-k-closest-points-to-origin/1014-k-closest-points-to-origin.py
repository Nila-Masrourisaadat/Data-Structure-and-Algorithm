class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distance=[]
        for i,(x,y) in enumerate(points):
            distance.append((x**2+y**2,i))
        #sort based on the first element of the tuples in the array distance
        distance.sort(key=lambda x:x[0] )
        return [points[dis[1]] for dis in distance[:k]]