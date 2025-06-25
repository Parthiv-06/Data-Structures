class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def sort_012(head):
    dummy=Node(0)
    temp0=dummy
    dummy1=Node(0)
    temp1=dummy1
    dummy2=Node(0)
    temp2=dummy2
    temp=head
    while temp is not None:
        if temp.data==0:
            temp0.next=temp
            temp0=temp0.next
        elif temp.data==1:
            temp1.next=temp
            temp1=temp1.next
        else:
            temp2.next=temp
            temp2=temp2.next
        temp=temp.next
    temp0.next=dummy1.next
    temp1.next=dummy2.next
    return dummy.next
def printll(head):
    printval=head
    while printval is not None:
        print(printval.data,end=" ")
        printval=printval.next
    return head
def array_to_ll(arr):
    head=Node(arr[0])
    mover=head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
    return head
arr=[0,1,2,1,0,2,0,1,2,0,0]
head=array_to_ll(arr)
head=sort_012(head)
printll(head)