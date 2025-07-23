def target_sum(res,tar,arr,n,i):
    if i==n:
        return False 
    res.append(arr[i])
    if sum(res)==tar:
        print(res)
        return True
    target_sum(res,tar,arr,n,i+1)
    res.remove(arr[i])
    if sum(res)==tar:
        print(res)
        return True
    target_sum(res,tar,arr,n,i+1)
arr=[1,2,2,3,4]
res=[]
tar=4
target_sum(res,tar,arr,len(arr),0)

    