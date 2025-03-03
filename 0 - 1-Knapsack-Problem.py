'''You are given the weights and values of items, and you need to put these items in a knapsack of capacity capacity to achieve the maximum total value in the knapsack. Each item is available in only one quantity.
In other words, you are given two integer arrays val[] and wt[], which represent the values and weights associated with items, respectively. You are also given an integer capacity, which represents the knapsack capacity. Your task is to find the maximum sum of values of a subset of val[] such that the sum of the weights of the corresponding subset is less than or equal to capacity. You cannot break an item; you must either pick the entire item or leave it (0-1 property).

Input: capacity = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1] 
Output: 3
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.

Input: capacity = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] 
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).

Input: capacity = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 6, 3] 
Output: 50
Explanation: Choose the last item (value 50, weight 3) for a total value of 50.'''

class Solution:
    def knapSack(self, capacity, val, wt):
        n=len(val)
        dp=[[0]*(capacity+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(capacity+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(dp[i-1][j],(val[i-1]+dp[i-1][j-wt[i-1]]))
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
        
