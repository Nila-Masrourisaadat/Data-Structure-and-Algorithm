class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #better
        intervals.sort()
        cnt=0
        prev_end=intervals[0][1]
        for start, end in intervals[1:]:
            if start>=prev_end:
                #non overlapping
                prev_end=end
            else: #overlapping
                cnt+=1
                prev_end=min(prev_end, end)
        return cnt

        #mine:
        sorted_intervals=sorted(intervals, key=lambda x:x[0])
        prev=sorted_intervals[0]
        cnt=0
        for i,(next_s, next_e)in enumerate(sorted_intervals[1:]):
            start,end=prev[0],prev[1]
            #check if they overlap
            if start<=next_s<end or start<next_e<=end:
                if end<next_e or (end==next_e and start>next_s):
                    prev=[start,end]
                else:
                    prev=[next_s,next_e]
                cnt+=1
            else:
                prev=[next_s,next_e]
                
        return cnt

