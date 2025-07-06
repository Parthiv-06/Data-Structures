def jump_game2(arr):
    near,far=0,0
    jumps=0
    while far<len(arr)-1:
        farthest=0
        print(near,far)
        for i in range(near,far+1):
            farthest=max(farthest,i+arr[i])
        near=far
        far=farthest
        jumps+=1
    return jumps
arr=[2,3,0,2,1,3,0,4]
print(jump_game2(arr))