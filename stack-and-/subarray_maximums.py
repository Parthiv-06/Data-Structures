def next_greater_el(a):
    stack=[]
    res=[0]*len(a)
    for i in range(len(a)-1,-1,-1):
        while len(stack)!=0 and a[stack[-1]]<a[i]:
            stack.pop()
        if len(stack)==0:
            res[i]=len(a)
        else:
            res[i]=stack[-1]
        stack.append(i)
    return res
def previous_greater_el(a):
    res=[0]*len(a)
    stack=[]
    for i in range(len(a)):
        while len(stack)!=0 and a[stack[-1]]<a[i]:
            stack.pop()
        if len(stack)==0:
            res[i]=-1
        else:
            res[i]=stack[-1]
        stack.append(i)
    return res
def subarray_maximums_sum(arr):
    pgee=previous_greater_el(arr)
    nge=next_greater_el(arr)
    total=0
    for i in range(len(arr)):
        left=i-pgee[i] 
        right=nge[i]-i 
        total+=(left*right*arr[i])
    return total
arr=[6,0,8,1,3]
print(subarray_maximums_sum(arr)) 