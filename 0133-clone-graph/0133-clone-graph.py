"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        def dfs(node, deep_copy):
            if node.val in deep_copy:
                return
            deep_copy[node.val]=Node(node.val)
            for neighbor in node.neighbors:
                if neighbor.val not in deep_copy:
                    dfs(neighbor,deep_copy)
                deep_copy[node.val].neighbors.append(deep_copy[neighbor.val])
        deep_copy={}            
        dfs(node,deep_copy)
        return deep_copy[node.val] 