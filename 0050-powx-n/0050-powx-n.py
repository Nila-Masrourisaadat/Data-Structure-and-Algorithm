class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==0:
            return self.myPow(x*x,n/2)
        return self.myPow(x*x,n/2)*x


        if n<0:
            x=1/x
            n=-n
        res=x
        def pow(res,n):
            if n==0:
                return 1
            elif n==1:
                return res
            else: 
                return pow(res*x,n-1)
           
        return pow(res,n)

        #whats the time complexity and how is it different from iteration?