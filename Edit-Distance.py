'''Given two strings s1 and s2. Return the minimum number of operations required to convert s1 to s2.

The possible operations are permitted:
Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.

Input: s1 = "geek", s2 = "gesek"
Output: 1
Explanation: One operation is required, inserting 's' between two 'e' in s1.

Input: s1 = "gfg", s2 = "gfg"
Output: 0

Input: s1 = "abcd", s2 = "bcfe"
Output: 3
Explanation: We can convert s1 into s2 by removing ‘a’, replacing ‘d’ with ‘f’ and inserting ‘e’ at the end. 

1 ≤ s1.length(), s2.length() ≤ 103'''

class Solution:
	def editDistance(self, s1, s2):
		dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
		    
		for i in range(0,len(s1)+1): 
		    dp[i][0]=i
		    
		for j in range(0,len(s2)+1):
		    dp[0][j]=j
		    
		    
		for i in range(1,len(s1)+1):
		    for j in range(1,len(s2)+1):
		        if s1[i-1]==s2[j-1]:
		            dp[i][j]=dp[i-1][j-1]
		        else:
		            dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1

		return dp[-1][-1]
