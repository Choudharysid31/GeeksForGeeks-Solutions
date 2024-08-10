'''Given an array arr[] that contains n integers (may be positive, negative or zero). Find the product of the maximum product subarray.
Note: It is guarenteed that the output fits in 64-bit integer.
Examples
Input: arr[] = {6, -3, -10, 0, 2}, n = 5
Output: 180
Explanation:  The subarray [6, -3, -10] gives max product as 180.
Input: arr[] = {2, 3, 4, 5, -1, 0}, n = 6
Output: 120
Explanation: The subarray [2, 3, 4, 5] gives max product as 120.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

class Solution:
	def maxProduct(self,arr, n):
		curr_prod=1
		neg_prod=1
		max_prod=-float("inf")
		for i in range(n):
		    curr_prod=arr[i]*curr_prod
		    neg_prod=arr[n-1-i]*neg_prod
		    max_prod=max(max_prod,curr_prod,neg_prod)
		    if curr_prod==0:
		        curr_prod=1
		    if neg_prod==0:
		        neg_prod=1
		return max_prod
