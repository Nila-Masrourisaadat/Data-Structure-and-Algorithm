class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #union find
        #always with parents and ranks array to keep track of parents of each node and the number of nodes in each cluster respectively
        par=[i for i in range(n)]# at first each node is its own parent
        rank=[1]*n#at first we have n components if we consider each node its own disconnected component 

        # parent of a parent of a node can be a parent of a node
        def find(n1):#to find the parent of a node
            res=n1
            while res!=par[res]: #we can stop searching when the node itself is its own parent because that means we cant go any higher, we found the root parent
                par[res]=par[par[res]] #path compression
                res=par[res] #move up the chain
            return res
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0#they are already connected
            # we wanna merge the nodes but we wanna merge the smaller size cluster with the bigger one
            if rank[p1]<rank[p2]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=rank[p2]
            return 1

        cnt=n
        for n1,n2 in edges:
            cnt-=union(n1,n2)
        
        return cnt


                

