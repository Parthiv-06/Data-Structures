# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next
# def find_middle(head):
#     slow=head
#     fast=head
#     while fast is not None and fast.next is not None:
#         slow=slow.next
#         fast=fast.next
#     return slow
# def array_to_ll(a):
#     head=Node(a[0])
#     mover=head
#     for i in range(1,len(a)):
#         temp=Node(a[i])
#         mover.next=temp
#         mover=temp
#     return head
# def mergesortedLinkedList(list1,list2):
#     dummy=Node(-1)
#     temp=dummy
#     while list1 is not None and list2 is not None:
#         if list1.data <= list2.data:
#             temp.next=list1
#             list1=list1.next
#         else:
#             temp.next=list2
#             list2=list2.next
#         temp=temp.next
#     if list1 is not None:
#         temp.next=list1
#     if list2 is not None:
#         temp.next=list2
#     return dummy.next
# def sortll(head):
#     middle=find_middle(head)
#     left=head
#     right=middle.next
#     middle.next=None
#     left=sortll(left)
#     right=sortll(right)
#     return mergesortedLinkedList(left,right)
# def printll(head):
#     printval=head
#     while printval is not None:
#         print(printval.data,end=" ")
#         printval=printval.next
#     return head
# a=[4,2,5,6,7,1,9,0,8]
# head=array_to_ll(a)
# printll(head)
# print("\n")
# sortll(head)
# printll(head)

    
                                
                     
# Node class represents a
# node in a linked list
class Node:
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        
        # Pointer to the next node in the list
        self.next = next1

# Function to merge two sorted linked lists
def mergeTwoSortedLinkedLists(list1, list2):
    # Create a dummy node to serve
    # as the head of the merged list
    dummyNode = Node(-1)
    temp = dummyNode

    # Traverse both lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare elements of both lists and
        # link the smaller node to the merged list
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        # Move the temporary pointer
        # to the next node
        temp = temp.next 

    # If any list still has remaining
    # elements, append them to the merged list
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    
    # Return the merged list starting 
    # from the next of the dummy node
    return dummyNode.next

# Function to find the middle of a linked list
def findMiddle(head):
    # If the list is empty or has only one node
    # the middle is the head itself
    if head is None or head.next is None:
        return head

    # Initializing slow and fast pointers
    slow = head
    fast = head.next

    # Move the fast pointer twice as
    # fast as the slow pointer

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    # When the fast pointer reaches the end,
    # the slow pointer will be at the middle

    return slow

# Function to perform merge sort on a linked list
def sortLL(head):
    # Base case: if the list is empty
    # or has only one node it is already 
    # sorted, so return the head
    if head is None or head.next is None:
        return head

    # Find the middle of the list
    # using the findMiddle function
    middle = findMiddle(head)

    # Divide the list into two halves
    right = middle.next
    middle.next = None
    left = head

    # Recursively sort the left and right halves
    left = sortLL(left)
    right = sortLL(right)

    # Merge the sorted halves using
    # the mergeTwoSortedLinkedLists function
    return mergeTwoSortedLinkedLists(left, right)

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

# Linked List: 3 2 5 4 1
head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print("Original Linked List: ", end="")
printLinkedList(head)

# Sort the linked list
head = sortLL(head)

print("Sorted Linked List: ", end="")
printLinkedList(head)

                                
                            