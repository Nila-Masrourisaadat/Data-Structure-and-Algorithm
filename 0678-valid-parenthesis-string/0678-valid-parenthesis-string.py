class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        minleft=0
        maxleft=0
        for i, par in enumerate(s):
            if par=="(":
                maxleft,minleft=maxleft+1,minleft+1
            elif par==")":
                maxleft,minleft=maxleft-1,minleft-1
            else:
                maxleft,minleft=maxleft+1,minleft-1
            if maxleft<0:
                return False
            if minleft<0: #s="(*)("
                minleft=0
        return minleft==0
            

                      
