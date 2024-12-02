class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand)%groupSize!=0:
            return False
        hand.sort()

        counter={}
        for h in hand:
            counter[h]=counter.get(h,0)+1
        print(counter)
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

        





        # gpcounter=0
        # cnt=0
        # prev=0
        # visit=set()
        # i=0
        # while i<len(hand):
        #     if gpcounter<groupSize and prev!=hand[i] and i not in visit:
        #         prev=hand[i]
        #         visit.add(hand[i])
        #         gpcounter+=1
        #         i+=1
        #     elif prev==hand[i] and cnt==0:
        #         cnt+=1
        #         tmp=i
        #         i+=1
        #     elif gpcounter>=groupSize:
        #         cnt==0
        #         gpcounter=0
        #         prev=0
        #         i=tmp
        # return False if gpcounter!=groupSize else True
            