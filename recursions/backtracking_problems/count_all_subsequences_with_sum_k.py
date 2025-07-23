def count_of_sum(arr,n,s,i,k):
    if i==n:
        if s==k:
            return 1
        return 0
    s+=arr[i]
    l=count_of_sum(arr,n,s,i+1,k)
    s-=arr[i]
    r=count_of_sum(arr,n,s,i+1,k)
    return l+r
arr=[1,2,1]
k=3

s=0
print(count_of_sum(arr,len(arr),s,0,k))