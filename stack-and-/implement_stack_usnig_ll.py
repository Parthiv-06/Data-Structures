class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Stack:
    def __init__(self):
        self.size=0
        self.top=None

    def push(self,val):
        new_node=Node(val)
        if self.top is None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        print("pushedd: ",new_node.data)
        self.size+=1
    def pop(self):
        if self.top is None:
            print("stack is empty: ")
            exit(1)
        temp=self.top
        self.top=self.top.next
        temp.next=None
        print("popped : ",temp.data)
        del temp
        self.size-=1
    def size_of_stack(self):
        print("size of stack is : ",self.size)
    def top_el(self):
        print("top element is : ",self.top.data)
    def print_stack(self):
        printval=self.top
        while printval is not None:
            print(printval.data,end=" ")
            printval=printval.next
        return self.top
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.size_of_stack()
s.top_el()
s.print_stack()