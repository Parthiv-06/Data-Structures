class Node:
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1
class SLL:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        printval=self.head
        while printval is not None:
            print(printval.data,end=" ")
            printval=printval.next
l=SLL()
l.head=Node(10)
e2=Node(20)
e3=Node(30)
l.head.next=e2
e2.next=e3
SLL.printlinkedlist(l)

    