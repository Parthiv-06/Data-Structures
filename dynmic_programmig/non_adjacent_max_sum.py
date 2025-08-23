def no_adjacent_max_sum(arr,ind):
    prev=arr[0]
    prev2=0
    for i in range(1,ind):
        pick=arr[i]        
        if i>1:
            pick+=prev2
        non_pick=0+prev
        curr_i=max(pick,non_pick)
        print(curr_i,prev,prev2)
        prev2=prev
        prev=curr_i
    return curr_i
arr=[2,1,4,9]
print(no_adjacent_max_sum(arr,4))