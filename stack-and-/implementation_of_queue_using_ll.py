class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.start=None
        self.end=None
        self.size=0
    def push(self,val):
        new_node=Node(val)
        if self.start is None :
            self.start=new_node
            self.end=new_node
        else:
            self.end.next=new_node
            self.end=self.end.next
        self.size+=1
    def pop(self):
        if self.start is None:
            print("the queue is empty: ")
            exit(1)
        temp=self.start
        self.start=self.start.next
        temp.next=None
        print("popped: ",temp.data)
        self.size-=1
    def size_of_queue(self):
        print("size of queue is : ",self.size)
    def top_el(self):
        print("top element is : ",self.start.data)
q=Queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.pop()
q.pop()