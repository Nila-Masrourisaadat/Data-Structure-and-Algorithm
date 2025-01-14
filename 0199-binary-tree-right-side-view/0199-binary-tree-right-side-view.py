# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #bfs
        # q = deque()
        # res=[]
        # q.append(root)
        # if not root:
        #     return []
        # while q:
        #     size=len(q)
        #     for i in range(size):
        #         node=q.popleft()
        #         if i==size-1:
        #             res.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
                
        # return res
            
        #dfs
        
        result = []

        def dfs(node, level):
            # Base case: If the node is None, return
            if not node:
                return
            
            # If this is the first node of this level, add it to the result
            if len(result) == level:
                result.append(node.val)
            
            # Recursively call the function on the right and then the left child
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result

