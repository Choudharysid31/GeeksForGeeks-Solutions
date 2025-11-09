'''Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the last stair. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the last stair.

Input: heights[] = [20, 30, 40, 20]
Output: 20
Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
jump from stair 0 to 1: cost = |30 - 20| = 10, jump from stair 1 to 3: cost = |20 - 30| = 10 , Total Cost = 10 + 10 = 20

Input: heights[] = [30, 20, 50, 10, 40]
Output: 30

Constraints:
1 ≤ height.size() ≤ 105
0 ≤ height[i] ≤ 104'''

class Solution:
    def minCost(self, height):
        dp=[0]*len(height)
        if len(height)>1:
            dp[-2]=abs(height[-2]-height[-1])
        for i in range(len(height)-3,-1,-1):
            dp[i]=min(abs(height[i+2]-height[i])+dp[i+2],abs(height[i+1]-height[i])+dp[i+1])
            
        return dp[0]
            
