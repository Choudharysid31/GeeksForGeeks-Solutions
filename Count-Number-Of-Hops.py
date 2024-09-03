'''A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top of Nth step. As the answer will be large find the answer modulo 1000000007.

Input: N = 1
Output: 1

Input:
N = 4
Output: 7
Explanation:Below are the 7 ways to reach 4
1 step + 1 step + 1 step + 1 step
1 step + 2 step + 1 step
2 step + 1 step + 1 step
1 step + 1 step + 2 step
2 step + 2 step
3 step + 1 step
1 step + 3 step

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).'''

class Solution:
    def countWays(self,n):
        if n<3:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        dp[3]=4
        for i in range(4,n+1):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000007
        return dp[n]
