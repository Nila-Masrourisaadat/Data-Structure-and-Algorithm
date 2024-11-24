# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt=0
        def dfs(node,mx):
            if not node:
                return 0
            if node.val>=mx:
                cnt=1
                mx=node.val 
            else:
                cnt=0
            left=dfs(node.left,mx)
            right=dfs(node.right,mx)
            cnt+=left+right

            return cnt
        
        return dfs(root,root.val)
        
