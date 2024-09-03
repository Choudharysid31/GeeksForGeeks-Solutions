'''Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 

Input: N = 5, arr[] = {1, 101, 2, 3, 100} 
Output: 106
Explanation: The maximum sum of a increasing sequence is obtained from {1, 2, 3, 100},

Input: 
N = 4, arr[] = {4, 1, 2, 3}
Output: 6
Explanation:The maximum sum of a increasing sequence is obtained from {1, 2, 3}.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)'''

class Solution:
	def maxSumIS(self, Arr, n):
		dp=Arr[:]
		for i in range(1,n):
		    for j in range(i):
		        if Arr[i]>Arr[j] and dp[i]<Arr[i]+dp[j]:
		            dp[i]=Arr[i]+dp[j]
	    return max(dp)
		    
