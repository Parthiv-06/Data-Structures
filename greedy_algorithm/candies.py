def candies_problem(arr):
    candies=[1]*len(arr)
    for i in range(len(arr)):
        if arr[i]>arr[i-1]:
            candies[i]=candies[i-1]+1
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>arr[i+1]:
            candies[i]=max(candies[i],candies[i+1]+1)
    return sum(candies)
arr=[1,2,3,0,4]
print(candies_problem(arr))