# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        #O(n) time complexity
        #O(n) space complexity
        # arr=[]
        # while head:
        #     arr.append(head.val)
        #     head=head.next
        # print(arr)
        # l,r=0,len(arr)-1
        # while l<=r:
        #     if arr[l]!=arr[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True

        #O(n) time complexity
        #O(1) space complexity

        #slow and fast pointer to find the middle 
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        #reverse the second half of linked list because in singly linked list we can only move left and when second half is reversed we can traverse the first and second half at the same time and compare
        prev=None
        while slow:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        
        #now we traverse the first half and reversed second half of the linked list at the same time to compare
        left,right=head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True


      