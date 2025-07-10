class job_sequence:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit
class Solution:
    def highest_profit(arr):
        arr.sort(key=lambda x:x.profit,reverse=True)
        max_deadline=arr[0].deadline
        for i in range(len(arr)):
            max_deadline=max(max_deadline,arr[i].deadline)
        cnt_jobs=0
        cnt_profit=0
        slot=[-1]*(max_deadline+1)

        for i in range(len(arr)):
            for j in range(arr[i].deadline,0,-1):
                if slot[j]==-1:
                    slot[j]=i
                    cnt_jobs+=1
                    cnt_profit+=arr[i].profit
                    
                    break
        return cnt_jobs,cnt_profit

arr=[job_sequence(1,2,100),job_sequence(2,1,19),job_sequence(3,2,27),job_sequence(4,1,25),job_sequence(5,1,15)]
print(Solution.highest_profit(arr))