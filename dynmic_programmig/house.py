def house_robbery(arr,ind):
    prev=arr[0]
    prev2=0
    for i in range(1,ind):
        pick=arr[i]
        if i>1:
            pick+=prev2
        non_pick=0+prev
        curr=max(pick,non_pick)
        prev2=prev
        prev=curr
    return prev
def house_robb(arr,ind):
    arr1=[]
    arr2=[]
    for i in range(ind):
        if i!=0:
            arr1.append(arr[i])
        if i!=(ind-1):
            arr2.append(arr[ind])
    ans1=house_robbery(arr1,ind)
    ans2=house_robbery(arr2,ind)
    return max(ans1,ans2)
arr= [1, 5, 1, 2, 6]
n=len(arr)
print(house_robbery(arr,n))
