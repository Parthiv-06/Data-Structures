def job_waiting_time(arr):
    waiting_time=0
    total_time=0
    arr.sort()
    for i in range(len(arr)):
        waiting_time+=total_time
        total_time+=arr[i]
    return waiting_time//len(arr)
arr=[1,2,3,4,5]
print(job_waiting_time(arr))