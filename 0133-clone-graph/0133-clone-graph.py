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
        #we have to traverse the graph and create new nodes and copy old nodes value in them
        #input: reference of the first node of the graph->value = 1
        #output:copy of the given node as reference to the cloned graph
        if not node:
            return node
        dic={}
        def clone(node):
            if node in dic:
                return dic[node]
            ncopy=Node(node.val)#clone the node
            #add to hasmap to map the old one to the new one
            dic[node]=ncopy
            #now we go throught the neighbors to add them to the cloned node if they are already cloned and in the dictionary ,if not we have to clone them first
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    ncopy.neighbors.append(clone(neighbor))
                else:
                    ncopy.neighbors.append(dic[neighbor])
            return ncopy
        
        return clone(node)


        
        