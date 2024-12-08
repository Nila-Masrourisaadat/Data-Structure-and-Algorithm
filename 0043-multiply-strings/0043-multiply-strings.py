class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry,summ,res=0,0,0
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                mul=(int(num1[i])*int(num2[j])+carry)
                carry=mul//10
                summ+=(mul%10)*(10**(len(num2)-j-1))
                # print(num1[i],num2[j],(mul%10)*(10**(len(num1)-i-1)),carry,summ)
            summ+=carry*(10**len(num2))
            # print(summ)   
            res+=summ*(10**(len(num1)-i-1))
            summ=0
            carry=0
        return str(res)