def print_all_subsequences(res,arr,i,n):
    if i==n:
        print(res)
        return 
    res.append(arr[i])
    print_all_subsequences(res,arr,i+1,n)
    res.remove(arr[i])
    print_all_subsequences(res,arr,i+1,n) 

arr=[1,2,3,4]
res=[]
print_all_subsequences(res,arr,0,len(arr))
