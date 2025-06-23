class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def array_to_ll(a):
    head=Node(a[0])
    mover=head
    for i in range(1,len(a)):
        temp=Node(a[i])
        mover.next=temp
        mover=mover.next
    return head
def odd_even_nodes(head):
    idx=1
    odd=Node(0)
    odd_ptr=odd
    even=Node(0)
    even_ptr=even
    temp=head
    while temp is not None:
        if idx%2==0:
            even_ptr.next=temp
            even_ptr=even_ptr.next
        else:
            odd_ptr.next=temp
            odd_ptr=odd_ptr.next
        temp=temp.next
        idx+=1
    even_ptr.next=None
    odd_ptr.next=even
    return odd.next
def printll(head):
    printval=head
    while printval is not None:
        print(printval.data,end=" ")
        printval=printval.next
a=[10,20,30,40,50]
head=array_to_ll(a)
head=odd_even_nodes(head)
printll(head)
