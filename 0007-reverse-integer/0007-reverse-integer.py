class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=False
        if x<0:
            x=-x
            flag=True
        res=0
        while x:
            res=(x%10)+res*10
            x=x//10
            if x:
                if (not flag and res>(2**31-1)//10) or (flag and res>2**31//10):
                    return 0
                elif (not flag and res==(2**31-1)//10) or (flag and res==2**31//10):
                    if (not flag and x>(2**31-1)%10) or (flag and x>2**31%1010):
                        return 0
        return -res if flag else res

