def duplicates_in_n(arr):
    mpp={}
    for i in range(len(arr)):
        mpp[arr[i]]=mpp.get(mpp[arr[i]],0)+1
    for key,value in mpp.items():
        if value >1:
            return key
    return -1
arr=[1,2,3,4,3]
print(duplicates_in_n(arr))