'''There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum

Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.

Expected Time Complexity: O(n*k)
Expected Auxilary Space: O(n)'''

class Solution:
    def minimizeCost(self, k, arr):
        n=len(arr)
        dp=[0]*(n)
        for i in range(1,n):
            step=float('inf')
            for j in range(1,k+1):
                if i>=j:
                    step=min(step,dp[i-j]+abs(arr[i]-arr[i-j]))
                else:
                    break
            dp[i]=step
        return dp[-1]
