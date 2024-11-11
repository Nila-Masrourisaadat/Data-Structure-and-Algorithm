class Node(object):
    def __init__(self, key,val):
        self.val=val
        self.key=key
        self.next=self.prev=None



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache={}#hashamp
        #left is always pointing at LRU 
        self.left,self.right=Node(0,0),Node(0,0)
        #now connect the left and right in the begining
        self.left.next,self.right.prev=self.right,self.left########

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #when we get the key, it become used so it should move to the end of the linked list
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            #remove from LRU which left pointer is pointing at
            lru=self.left.next
            self.remove(lru)
            #also delete from the hashmap
            del self.cache[lru.key]

    #to remove the node
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    # to insert the node to the right most
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        node.next=nxt
        nxt.prev=node
        prev.next=node
        node.prev=prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)