class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust and n>1:
            return -1
        Adj=collections.defaultdict(list)
        potential_judge=0
        for (truster, trustee) in trust:
            Adj[truster].append(trustee)
        for i in range(1,n+1):
            print(i)
            if i not in Adj:
                potential_judge=i
        print(Adj)
        if potential_judge==0:
            print("here")
            return -1
        for truster,trustee in Adj.items():
            if potential_judge not in Adj[truster]:
                print("here2")
                return -1
        return potential_judge