class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x==0:
            return 0
        l,r=1,x
        while l<=r:
            m=(l+r)//2
            if x<m*m:
                r=m-1
            elif x>m*m:
                l=m+1
            else:
                return m
        print(m)       
        if (m)*(m)<x:
            return m
        if (m-1)*(m-1)<x:
            return m-1
        

