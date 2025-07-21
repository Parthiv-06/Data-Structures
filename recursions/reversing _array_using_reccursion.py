def reverse(arr,n,i):
    if i>=n//2:
        print(arr)
        return 
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    return reverse(arr,n,i+1)
arr=[1,2,3,4,5]
reverse(arr,5,0)