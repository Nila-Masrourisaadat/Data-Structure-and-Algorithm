# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        career=0
        prev=None
        while l1 and l2:
            l3=ListNode((l1.val+l2.val+career)%10)
            if prev:
                prev.next=l3
            else:
                head=l3
            career=(l1.val+l2.val+career)//10
            prev=l3
            l1=l1.next
            l2=l2.next
        while l1:
            l3=ListNode((l1.val+career)%10)
            prev.next=l3
            career=(l1.val+career)//10
            prev=l3
            l1=l1.next
        while l2:
            l3=ListNode((l2.val+career)%10)
            prev.next=l3
            career=(l2.val+career)//10
            prev=l3
            l2=l2.next
        while career//10!=0 or career%100!=0:
            l3=ListNode(career%10)
            prev.next=l3
            career=(career)//10
            prev=l3
        return head