# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node,res):
            if not node:
                return
            dfs(node.left,res)
            res.append(node.val)
            dfs(node.right,res)
        res=[]
        dfs(root,res)
        return res

         #recursive
        # res=[]
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        
        # inorder(root)
        # return res

        #iterative
        stack=[]
        res=[]
        node=root
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            res.append(node.val)
            node=node.right
             
        return res
            
#why is iterative faster thank recursive?


