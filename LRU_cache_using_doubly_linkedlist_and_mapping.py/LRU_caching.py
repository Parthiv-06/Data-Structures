class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LRU_caching:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.oldest=Node(0,0)
        self.newest=Node(0,0)
        self.oldest.next=self.newest
        self.newest.prev=self.oldest
    def insert(self,node):
        n,p=self.newest,self.newest.prev
        n.prev=Node
        node.prev=p
        p.next=node
        node.next=n
    def remove(self,node):
        n,p=node.next,node.prev
        p.next=n
        n.prev=p
    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            print( self.cache[key].val)
        else:
            return -1
        
    def put(self,key,val):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,val)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.oldest.next
            self.remove(lru)
            del self.cache[lru]
l=LRU_caching(4)
l.put(2,6)
l.put(5,6)
l.put(8,5)
l.get(2)
l.get(7)
l.put(7,8)