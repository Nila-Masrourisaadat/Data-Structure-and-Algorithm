class DetectSquares(object):

    def __init__(self):
        self.counter={}
        self.plane=[]
    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.counter[tuple(point)]=self.counter.get(tuple(point),0)+1
        self.plane.append(point)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        count=0
        for (x,y) in self.plane:
            if x==point[0] or y==point[1]:
                continue
            if abs(point[0]-x)==abs(point[1]-y):
                if (x,point[1]) in self.counter and (point[0],y) in self.counter:
                    count+=self.counter[(x,point[1])]*self.counter[(point[0],y)]
        return count




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)