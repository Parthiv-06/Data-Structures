def nextGreaterElement(nums1,nums2):
    stack=[]
    mpp={}
    res=[0]*len(nums1)
    for i in range(len(nums2)-1,-1,-1):
        while len(stack)!=0 and stack[-1]<nums2[i]:
            stack.pop()
        if len(stack)==0:
            mpp[nums2[i]]=mpp.get(nums2[i],0)-1
        elif stack[-1]>nums2[i]:
            mpp[nums2[i]]=stack[-1] 
        stack.append(nums2[i])
    print(mpp)
    for i in range(len(nums1)):
        res[i]=mpp[nums1[i]]   
    return res     

nums1=[4,1,2]
nums2=[1,3,4,2]
print(nextGreaterElement(nums1,nums2))