'''Given an integer n denoting the Length of a line segment. You need to cut the line segment in such a way that the cut length of a line segment each time is either x , y or z. Here x, y, and z are integers. After performing all the cut operations, your total number of cut segments must be maximum. Return the maximum number of cut segments possible.

Note: if no segment can be cut then return 0.

Input: n = 4, x = 2, y = 1, z = 1
Output: 4
Explanation: Total length is 4, and the cut lengths are 2, 1 and 1.  We can make maximum 4 segments each of length 1.

Input: n = 5, x = 5, y = 3, z = 2
Output: 2
Explanation: Here total length is 5, and the cut lengths are 5, 3 and 2. We can make two segments of lengths 3 and 2.

Input: n = 7, x = 8, y = 9, z = 10
Output: 0
Explanation: Here the total length is 7, and the cut lengths are 8, 9, and 10. We cannot cut the segment into lengths that fully utilize the segment, so the output is 0.

1 <= n, x, y, z <= 104'''

class Solution:

    def maximizeTheCuts(self,n,x,y,z):
        dp=[-float("inf")]*(n+1)
		dp[0]=0
		for cut in (x,y,z) :
		    for j in range(cut,n+1):
		        dp[j]=max(dp[j],1+dp[j-cut])
	    return dp[-1] if dp[-1]!=-float("inf") else 0
