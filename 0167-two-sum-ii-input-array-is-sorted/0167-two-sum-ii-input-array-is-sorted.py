class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(numbers)-1

        while l<r:
            if numbers[r]+numbers[l]<target:
                print(1,numbers[l],numbers[r])
                l+=1
            if numbers[r]==target-numbers[l]:
                return [l+1,r+1]
            elif numbers[r]+numbers[l]>target:
                print(2,numbers[l]+numbers[r]<target,numbers[l],numbers[r])
                r-=1