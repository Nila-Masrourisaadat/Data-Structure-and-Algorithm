class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        #better
        if len(hand)%groupSize!=0:
            return False
        counter={}
        minheap=[]
        for h in hand:
            counter[h]=counter.get(h,0)+1
        for h in counter:
            heapq.heappush(minheap,h)
        
        while minheap:
            h=minheap[0]
            
            for i in range(h, h+groupSize):
                if i not in counter:
                    return False
                counter[i]-=1
                if counter[i]==0:
                    if i!=minheap[0]:#if the key that its value turned zero is not the min in minheap
                        return False
                    heapq.heappop(minheap)
        return True
                
        

        #mine
        if len(hand)%groupSize!=0:
            return False
        hand.sort()

        counter={}
        for h in hand:
            counter[h]=counter.get(h,0)+1
        i=0
        while i<len(hand):
            h=hand[i]
            if counter[h]==0:
                i+=1
                continue
            gpcounter=1
            counter[h]-=1
            while gpcounter<groupSize:
                if (h+1) in counter and counter[h+1]!=0:
                    counter[h+1]-=1
                    gpcounter+=1
                    h+=1
                else:
                    return False
            i+=1
        return True

        




