def nextt_greater_element_circular(a):
    res=[0]*len(a)
    stack=[]
    for i in range(2*len(a)-1,-1,-1):
        while len(stack)!=0 and stack[-1]<a[i%len(a)]:
            stack.pop()
        if i<len(a):
            if len(stack)==0:
                res[i]=-1
            elif stack[-1]>a[i]:
                res[i]=stack[-1]
        stack.append(a[i%len(a)])
    return res
a=[1,2,1]
print(nextt_greater_element_circular(a))
print(3%3)