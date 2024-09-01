'''Given an array arr of size n of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.
Note: Answer can be very large, so, output answer modulo 109+7.

Input: n = 6, arr = [5, 2, 3, 10, 6, 8], sum = 10
Output: 3
Explanation: {5, 2, 3}, {2, 8}, {10} are possible subsets.

Input: n = 5, arr = [2, 5, 1, 4, 3], sum = 10
Output: 3
Explanation: {2, 1, 4, 3}, {5, 1, 4}, {2, 5, 3} are possible subsets.

Expected Time Complexity: O(n*sum)
Expected Auxiliary Space: O(n*sum)'''

class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		dp = [[0] * (sum + 1) for _ in range(n+1)]
		for i in range(n):
		    dp[i][0]=1
		for i in range(1,sum+1):
		    dp[0][i]=0
		for i in range(1,n+1):
		    for j in range(sum+1):
		        if arr[i-1]<=j:
		            dp[i][j]=(dp[i-1][j]+dp[i-1][j-arr[i-1]])%1000000007
		        else:
		            dp[i][j]=dp[i-1][j]
		return dp[n][sum]
