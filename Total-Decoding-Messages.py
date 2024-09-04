'''A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1  'B' -> 2 ... 'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded, as the answer can be large return the answer modulo 109 + 7.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0s, extra trailing 0s and two or more consecutive 0s then it is an invalid string.

Input: str = "123"
Output: 3
Explanation: "123" can be decoded as "ABC"(123), "LC"(12 3) and "AW"(1 23).

Input: str = "90"
Output: 0
Explanation: "90" cannot be decoded as it's an invalid string and we cannot decode '0'.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(n) where n  = |str|'''

class Solution:
	def CountWays(self, str):
	    n=len(str)
	    dp=[0]*(n+1)
	    dp[0]=1
	    dp[1]=1
	    for i in range(2,n+1):
	        if str[i-1]!='0':
	            dp[i]=(dp[i-1])%1000000007
	        if str[i-2]=='1' or (str[i-2]=='2' and str[i-1]<='6'):
	            dp[i]=(dp[i]+dp[i-2])%1000000007
	    return dp[-1]
