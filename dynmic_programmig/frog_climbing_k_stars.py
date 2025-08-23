import sys
import math
def frog_climbing_k_stars(ind,k,arr,dp):
    if dp[ind]!=-1:
        return dp[ind]
    if ind==0:
        return 0
    res=sys.maxsize
    for i in range(1,k+1):
        if (ind-i)>=0:
            jump=frog_climbing_k_stars(ind-i,k,arr,dp)+abs(arr[ind]-arr[ind-i])
            res=min(res,jump)
    dp[ind]=res
    return dp[ind]
arr=[30,10,60,10,60,50]
k=2
dp=[-1]*len(arr)
n=len(arr)
print(frog_climbing_k_stars(n-1,k,arr,dp))

print(sys.maxsize)