# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=collections.deque()
        q.append(root)
        res=[[root.val]]
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    left=node.left
                    q.append(left)
                    level.append(left.val)
                if node.right:
                    right=node.right
                    q.append(right)
                    level.append(right.val)
            if level:
                res.append(level)
        return res


