class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        xt,yt,zt=target[0],target[1],target[2]
        x,y,z=0,0,0
        for i,(x1,y1,z1) in enumerate(triplets):
            if x1<=xt and y1<=yt and z1<=zt:
                x,y,z=max(x,x1),max(y,y1),max(z,z1)
            if x==xt and y==yt and z==zt:
                return True
            
        return False
            