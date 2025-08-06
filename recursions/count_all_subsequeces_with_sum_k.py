def sum_of_subsequece_k(arr,n,i,res,k):
    if i==n:
        if sum(res)==k:
            print(res)
        return
    res.append(arr[i])
    sum_of_subsequece_k(arr,n,i+1,res,k)
    res.remove(arr[i])
    sum_of_subsequece_k(arr,n,i+1,res,k)
arr=[1,2,3,1,2]
k=4
i=0
n=len(arr)
res=[]
sum_of_subsequece_k(arr,n,i,res,k)