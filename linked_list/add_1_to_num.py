class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def reverse_LinkedList(head):
    if head is None or head.next is None:
        return head
    new_head=reverse_LinkedList(head.next)
    front=head.next
    front.next=head
    head.next=None
    return new_head
def add_1(head):
    head=reverse_LinkedList(head)
    temp=head
    carry=1
    while temp is not None:
        if carry>0:
            if temp.data+carry>9:
                temp.data=0
                carry=1
            else:
                temp.data=temp.data+carry
                carry=0
        temp=temp.next
    head=reverse_LinkedList(head)
    return head
def array_to_ll(a):
    head=Node(a[0])
    mover=head
    for i in range(1,len(a)):
        temp=Node(a[i])
        mover.next=temp
        mover=temp
    return head
def print_LinkedList(head):
    printval=head
    while printval is not None:
        print(printval.data,end=" ")
        printval=printval.next
a=[1,9,9]
head=array_to_ll(a)
head=add_1(head)
print_LinkedList(head)