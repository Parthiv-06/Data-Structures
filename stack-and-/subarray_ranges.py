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
def previous_smaller_el(a):
    res=[0]*len(a)
    stack=[]
    for i in range(len(a)):
        while len(stack)!=0 and a[stack[-1]]>a[i]:
            stack.pop()
        if len(stack)==0:
            res[i]=-1
        else:
            res[i]=stack[-1]
        stack.append(i)
    return res
def next_smaller_el(a):
    res=[0]*len(a)
    stack=[]
    for i in range(len(a)-1,-1,-1):
        while len(stack)!=0 and a[stack[-1]]>a[i]:
            stack.pop()
        if len(stack)==0 :
            res[i]=len(a)
        else:
            res[i]=stack[-1]
        stack.append(i)
    return res
def subarray_ranges_sum(arr):
    nge=next_greater_el(arr)
    nse=next_smaller_el(arr)
    pge=previous_greater_el(arr)
    pse=previous_smaller_el(arr)
    total=0
    for i in range(len(arr)):
        ls=i-pse[i]
        rs=nse[i]-i
        lg=i-pge[i]
        rg=nge[i]-i
        total+=(lg*rg*arr[i])-(ls*rs*arr[i])
    return total
arr=[1,2,3]
print(subarray_ranges_sum(arr))