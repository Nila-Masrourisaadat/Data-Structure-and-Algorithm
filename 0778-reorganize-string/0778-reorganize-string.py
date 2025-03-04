class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=Counter(s)
        heap=[[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(heap)
        prev=None
        res=""
        while heap or prev:
            if prev and not heap:
                return ""
            #first pop the most frequent
            n,char=heapq.heappop(heap)
            #add it to the string
            res+=char
            #push the past prev back
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            
            #set the new prev
            if n+1!=0:
                #freeze/hold it
                prev=[n+1,char]
            
        return res
            