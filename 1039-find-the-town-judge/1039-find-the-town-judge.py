class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        incoming=defaultdict(int)
        outgoing=defaultdict(int)
        
        for truster, trustee in trust:
            outgoing[truster]=outgoing[truster]+1
            incoming[trustee]=incoming[trustee]+1
        for i in range(1,n+1):
            if incoming[i]==n-1 and outgoing[i]==0:
                return i
        return -1



        # if not trust and n>1:
        #     return -1
        # Adj=collections.defaultdict(list)
        # potential_judge=0
        # for (truster, trustee) in trust:
        #     Adj[truster].append(trustee)
        # for i in range(1,n+1):
        #     print(i)
        #     if i not in Adj:
        #         potential_judge=i
        # print(Adj)
        # if potential_judge==0:
        #     return -1
        # for truster,trustee in Adj.items():
        #     if potential_judge not in Adj[truster]:
        #         return -1
        # return potential_judge