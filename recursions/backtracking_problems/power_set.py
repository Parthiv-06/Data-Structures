def power_set(n,i,arr,res):
    if n==i:
        print(res)
        return
    res.append(arr[i])
    power_set(n,i+1,arr,res)
    res.remove(arr[i])
    power_set(n,i+1,arr,res)
arr=[1,2,3,4,5]
res=[]
n=len(arr)
power_set(n,0,arr,res)  