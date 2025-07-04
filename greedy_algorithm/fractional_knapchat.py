class items:
    def __init__(self,value,weight):
        self.weight=weight
        self.value=value
def fractional_knapchat(W,arr):
    arr.sort(key=lambda x:x.value/x.weight,reverse=True)
    curr_weight=0
    curr_val=0
    for i in range(len(arr)):
        if curr_weight+arr[i].weight<=W:
            curr_weight+=arr[i].weight
            print(curr_weight)
            curr_val+=arr[i].value
        else:
            curr_val+=(arr[i].value/arr[i].weight)*(W-curr_weight)
    return curr_val
W=90
arr=[items(100,20),items(60,10),items(100,50),items(200,50)]
val=fractional_knapchat(W,arr)
print(val)