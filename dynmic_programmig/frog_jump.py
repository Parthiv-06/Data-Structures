import sys

def frog_jump(i,arr,dp):
    if i==0:
        return 0
    if dp[i]!=-1:
        return dp[i]
    left=frog_jump(i-1,arr,dp)+abs(arr[i]-arr[i-1])
    right=sys.maxsize
    if i>1:
        right =frog_jump(i-2,arr,dp)+abs(arr[i]-arr[i-2])
    dp[i]=min(right,left)
    return dp[i]
arr=[10,20,30,10]
n=len(arr)
dp=[-1]*n
print(frog_jump(n-1,arr,dp))
print(dp)