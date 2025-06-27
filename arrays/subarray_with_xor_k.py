from collections import defaultdict

def subarray_with_xor_k(a,k):
    mpp=defaultdict(int)
    cnt=0
    xor=0
    mpp[xor]=1
    for i in range(len(a)):
        xor^=a[i]
        x=xor^k
        cnt+=mpp[x]
        mpp[xor]+=1
    return cnt
a=[4,2,2,6,4]
print(subarray_with_xor_k(a,6))