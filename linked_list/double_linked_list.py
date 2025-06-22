class Node:
    def __init__(self,data,next=None,back=None):
        self.data=data
        self.next=next
        self.back=back
class DLL:
    def __init__(self):
        self.head=None
    def double_linked_list(self,a):
        self.head=Node(a[0])
        prev=self.head
        for i in range(1,len(a)):
            temp=Node(a[i],None,prev)
            prev.next=temp
            prev=temp
        return self.head
    def printlinkedlist(self):
        printval=self.head
        while printval is not None:
            print(printval.data,end="<->")
            printval=printval.next
a=[10,20,30,40,50,60]
l=DLL()
DLL.double_linked_list(l,a)
DLL.printlinkedlist(l)