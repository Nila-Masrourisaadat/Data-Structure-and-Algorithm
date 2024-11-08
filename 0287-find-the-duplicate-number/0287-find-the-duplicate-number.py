class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:#cycle detection: they met somewhere in the cycle
                break
        #now we have to find the start of the cycle
        #why do we want to find the start of the cycle:
        #because thats where the duplicate is, why?
        #because duplicate is a node where its been pointed at from multiple other nodes because it has been in two indices in the array and the point where its been pointed at multiple times is the start of the cycle

        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
