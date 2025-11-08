'''Given a 2D array jobs[][] of size n × 3, where each row represents a single job with the following details:
jobs[i][0] : Start time of the job
jobs[i][1] : End time of the job
jobs[i][2] : Profit earned by completing the job

Find the maximum profit you can earn by scheduling non-overlapping jobs

Input: jobs[][] =  [[1, 2, 50], 
                 [3, 5, 20],
                 [6, 19, 100],
                 [2, 100, 200]] 
Output: 250
Explanation: The first and fourth jobs with the time range [1, 2] and [2, 100] can be chosen to give maximum profit of 50 + 200 = 250.

Input: jobs[][] =  [[1, 3, 60], 
                 [2, 5, 50],
                 [4, 6, 70],
                 [5, 7, 30]] 
Output: 130
Explanation: The first and third jobs with the time range [1, 3] and [4, 6] can be chosen to give maximum profit of 60 + 70 = 130.
Constraints:
1 ≤ jobs.size() ≤ 105
1 ≤ jobs[i][0] < jobs[i][1] ≤ 109
1 ≤ jobs[i][2] ≤ 104'''

class Solution: 
    def maxProfit(self, jobs):
        jobs.sort(key=lambda x:x[0])
        dp=[-1 for _ in range(len(jobs)+1)]
        dp[-1]=0
        for i in range(len(jobs)-1,-1,-1):
            
            next_avail=self.extend_bin(jobs,i)
            dp[i]=max(dp[i+1],jobs[i][2]+dp[next_avail])
        return dp[0]
            
    def extend_bin(self,jobs,start):
        
        left=0
        right=len(jobs)
        
        while left<right:
            mid=left+(right-left)//2
            
            if jobs[mid][0]<jobs[start][1]:
                left=mid+1
            else:
                right=mid
        return right
        
