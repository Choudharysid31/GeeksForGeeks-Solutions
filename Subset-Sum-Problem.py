'''Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

Input: n = 6, arr[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: 1 
Explanation: Here there exists a subset with sum = 9, 4+3+2 = 9.

Input: n = 6, arr[] = {3, 34, 4, 12, 5, 2} , sum = 30
Output: 0 
Explanation: There is no subset with sum 30.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function isSubsetSum() which takes the array arr[], its size N and an integer sum as input parameters and returns boolean value true if there exists a subset with given sum and false otherwise. The driver code itself prints 1, if returned value is true and prints 0 if returned value is false.

Expected Time Complexity: O(sum*n)
Expected Auxiliary Space: O(sum*n)'''

class Solution:
    def isSubsetSum (self, N, arr, sum):
		dp = [[0] * (sum + 1) for _ in range(N+1)]
		for i in range(N):
		    dp[i][0]=1
		for i in range(1,sum+1):
		    dp[0][i]=0
		for i in range(1,N+1):
		    for j in range(sum+1):
		        if arr[i-1]<=j:
		            dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
		        else:
		            dp[i][j]=dp[i-1][j]
		return dp[N][sum]
