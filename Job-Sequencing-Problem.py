'''Given a set of n jobs where each jobi has a deadline and profit associated with it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with a job if and only if the job is completed by its deadline.Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job. Deadline of the job is the time on or before which job needs to be completed to earn the profit.

Input: Jobs = [[1,4,20],[2,1,1],[3,1,40],[4,1,30]]
Output: 2 60
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).

Input: Jobs = [[1,2,100],[2,1,19],[3,2,27],[4,1,25],[5,1,15]]
Output: 2 127
Explanation: 2 jobs can be done with maximum profit of 127 (100+27).

Expected Time Complexity: O(nlogn)
Expected Auxilliary Space: O(n)'''

class Solution:
    def JobScheduling(self,Jobs,n):
        maxi=0
        brr=[]
        for i in Jobs:
            maxi=max(i.deadline,maxi)
            brr.append([i.profit,i.deadline])
        deadline=[True]*(maxi+1)
        brr.sort(reverse=True)
        count=0
        sume=0
        limit=0
        for i in brr:
            slot=i[1]
            if deadline[slot]:
                deadline[slot]=False
                count+=1
                sume+=i[0]
            else:
                while slot>0 and slot>limit:
                    if deadline[slot]:
                        deadline[slot]=False
                        count+=1
                        sume+=i[0]
                        break
                    slot-=1
                else:
                    limit=i[1]
        return [count,sume]
