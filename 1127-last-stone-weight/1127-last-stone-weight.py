class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        weights=[]
        for stone in stones:
            heapq.heappush(weights,-stone)
        
        while len(weights)>1:
            stone1=heapq.heappop(weights)
            stone2=heapq.heappop(weights)
            if stone1!=stone2:
                heapq.heappush(weights,stone1-stone2)
        
        return -weights[-1] if weights else 0



        
        
        