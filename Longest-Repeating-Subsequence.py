'''Given string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.
The two identified subsequences A and B can use the same ith character from string str if and only if that ith character has different indices in A and B. For example, A = "xax" and B = "xax" then the index of first "x" must be different in the original string for A and B.

Input: str = "axxzxy"
Output: 2
Explanation: The given array with indexes looks like
a x x z x y 
0 1 2 3 4 5
The longest subsequence is "xx". It appears twice as explained below.
subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str 
subsequence B
x x
0 1  <-- index of subsequence B
------
2 4  <-- index of str 
We are able to use character 'x' (at index 2 in str) in both subsequencesas it appears on index 1 in subsequence A and index 0 in subsequence B.

Input: str = "axxxy"
Output: 2
Explanation:The given array with indexes looks like
a x x x y 
0 1 2 3 4
The longest subsequence is "xx". It appears twice as explained below.

subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str 
subsequence B
x x
0 1  <-- index of subsequence B
------
2 3  <-- index of str 
We are able to use character 'x' (at index 2 in str) in both subsequences as it appears on index 1 in subsequence A and index 0 in subsequence B.

Expected Time Complexity: O(n2)
Expected Space Complexity: O(n2)'''

class Solution:
	def LongestRepeatingSubsequence(self, str):
	    n=len(str)
	    dp=[[0]*(n+1) for _ in range(n+1)]
	    for i in range(1,n+1):
	        for j in range(1,n+1):
	            if str[i-1]==str[j-1] and i!=j:
	                dp[i][j]=1+dp[i-1][j-1]
	            else:
	                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	    return dp[-1][-1]
