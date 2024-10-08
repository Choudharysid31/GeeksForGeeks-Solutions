'''Given an array arr of positive integers and another number x. Determine whether two elements exist in arr whose sum is exactly x or not. Return a boolean value true if two elements exist in arr else return false.

Examples:
Input: x = 16, arr[] = [1, 4, 45, 6, 10, 8]
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16
Input: x = 11, arr[] = [1, 2, 4, 3, 6]
Output: false
Explanation: None of the pair makes a sum of 11

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)'''

class Solution:
	def hasArrayTwoCandidates(self,arr, x):
	    dict={}
	    for i in arr:
	        if dict.get(x-i):
	            return True
	        dict[i]=1
	    return False
