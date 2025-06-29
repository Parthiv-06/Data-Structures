class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Queue:
    def __init__(self):
        self.start=None
        self.end=None
        self.size=0
    def push(self,val):
        New_node=Node(val)
        if self.start is None and self.end is None:
            self.start=New_node
            self.end=New_node
        else:
            self.end.next=New_node
            self.end=self.end.next
        # print("pushed: ",New_node.data)
        self.size+=1
    def pop(self):
        if self.start is None:
            print("The queue is empty: ")
            exit(1)
        else:
            temp=self.start
            self.start=self.start.next
            # print("poppedd: ",temp.data)
            temp.next=None
            del temp
            self.size-=1
    def size_of_queue(self):
        return self.size
    def top_element(self):
        print("top element is : ",self.start.data)
class Stack:
    def __init__(self):
        self.q=Queue()
    def push_in_stack(self,val):
        s=self.q.size_of_queue()
        self.q.push(val)
        if s is None:
            exit(1)
        for i in range(s):
            self.q.push(self.q.top_element)
            self.q.pop()
        pushed=self.q.top_element
        print("pushed : ",pushed)
    def pop_in_stack(self):
        print("popped: ",self.q.top_element)
        self.q.pop
    def top_element_in_stack(self):
        return self.q.top_element
    def size_of_stack(self):
        return self.q.size_of_queue
# q=Queue()
# q.push(10)
# q.push(20)
# q.push(30)
# q.push(40)
# q.push(40)
# q.pop()
# q.size_of_queue()
# q.top_element()

s=Stack()
s.push_in_stack(10)
s.push_in_stack(20)
s.push_in_stack(30)
s.push_in_stack(40)
s.pop_in_stack()
print(s.top_element_in_stack())