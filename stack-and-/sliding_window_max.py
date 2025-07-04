def maxSlidingWindow(nums,k):
    list=[]
    q=[]
    for i in range(len(nums)):
        if q and q[0] <=i-k:
            el=q[0]
            q.remove(el)
        while q and nums[q[-1]]<=nums[i]:
            q.pop()
        q.append(i)
        if i>=k-1:
            list.append(nums[q[0]])
    return list
nums=[1,3,-1,-3,5,3,6,7]
k=3
print(maxSlidingWindow(nums,k))