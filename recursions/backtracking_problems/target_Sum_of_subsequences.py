def sum_of_subsequence(arr,res,n,i,tar):
    if i==n:
        if sum(res)==tar:
            print(res)
        return 
    res.append(arr[i])
    sum_of_subsequence(arr,res,n,i+1,tar)
    res.remove(arr[i])
    sum_of_subsequence(arr,res,n,i+1,tar)

arr=[1,2,3,4]
tar=4
res=[]
sum_of_subsequence(arr,res,len(arr),0,tar)