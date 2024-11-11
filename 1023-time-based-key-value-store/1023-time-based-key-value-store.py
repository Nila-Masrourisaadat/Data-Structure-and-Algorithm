class TimeMap(object):

    def __init__(self):
        self.timemap=collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timemap[key].append((timestamp,value))


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr=self.timemap[key]
        l,r=0,len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid][0]==timestamp:
                return arr[mid][1]
            elif arr[mid][0]<timestamp:
                l=mid+1
            else:
                r=mid-1
        if 0<=r<len(arr) and arr[r][0]<timestamp:
            return arr[r][1]
        # if 0<l<len(arr) and arr[l][0]<timestamp:
        #     return arr[l][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)