class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res=[]
        carry=1
        for i in range(len(digits)-1,-1,-1):
            res.append((digits[i]+carry)%10)
            carry=(digits[i]+carry)//10

        if carry:
            res.append(carry)
        return res[::-1]

