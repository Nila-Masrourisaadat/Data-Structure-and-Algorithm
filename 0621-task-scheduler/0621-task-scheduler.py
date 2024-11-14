class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter={}
        q=collections.deque()
        h=[]
        time=0
        for task in tasks:
            counter[task]=counter.get(task,0)+1

        for key in counter:
            heapq.heappush(h, -counter[key])#negated because its minheap

        while q or h:
            time+=1
            
            if h:
                cnt=heapq.heappop(h)
                if cnt+1<0:
                    q.append((cnt+1,time+n))
            if q and q[0][1]==time:
                cnt,time=q.popleft()#remember cnt is negative
                heapq.heappush(h,cnt)
            
        return time
                