"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # mapping={}
        # def copy(node):
        #     if not node:
        #         return None
        #     if node in mapping:
        #         return mapping[node]
        #     mapping[node]=Node(node.val,copy(node.next),copy(node.random))
        #     # if node not in mapping:
        #     #     mapping[node]=nodecopy
        #     return mapping[node]

        # return copy(head)
        if not head:
            return None
        mapping={}
        node=head
        while node:
            mapping[node]=Node(node.val)
            node=node.next
        headcopy=head
        while headcopy:
            if headcopy.next:
                mapping[headcopy].next=mapping[headcopy.next]
            if headcopy.random:
                mapping[headcopy].random=mapping[headcopy.random]
            headcopy=headcopy.next
        return mapping[head]

