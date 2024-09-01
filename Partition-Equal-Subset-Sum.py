'''Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation: The two parts are {1, 5, 5} and {11}.

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be partitioned into two such parts.

Your Task:You do not need to read input or print anything. Your task is to complete the function equalPartition() which takes the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise, returns 0.

Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(sum of elements)'''

class Solution:
    def equalPartition(self, N, arr):
        target=sum(arr)
        if target%2==1:
            return 0
        target=target//2
        dp = [[0] * (target + 1) for _ in range(N+1)]
		for i in range(N):
		    dp[i][0]=1
		for i in range(1,target+1):
		    dp[0][i]=0
		for i in range(1,N+1):
		    for j in range(target+1):
		        if arr[i-1]<=j:
		            dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
		        else:
		            dp[i][j]=dp[i-1][j]
		return dp[N][target]
