'''There are N points on the road, you can step ahead by 1 or 2 . If you start from a point 0, and can only move from point i to point i+1 after taking a step of length one, find the number of ways you can reach at point N and returns the total number of ways modulo 109 + 7 to reach at Nth point.

Input: N = 4
Output: 5
Explanation: Number of ways to reach at 4th
point are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.

Input: N = 5
Output: 8

Expected Time Complexity: O(N)
Expected Space Complexity: O(N)'''

class Solution:
	def nthPoint(self,n):
		arr=[0]*(n+1)
		if n<3:
		    return n
		arr[1]=1
		arr[2]=2
		for i in range(3,n+1):
		    arr[i]=(arr[i-1]+arr[i-2])%1000000007
		return arr[n]
