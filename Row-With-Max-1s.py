'''Given a boolean 2D array, consisting of only 1's and 0's, where each row is sorted. Return the 0-based index of the first row that has the most number of 1s. 
If no such row exists, return -1.
Examples:
Input: arr[][] = [[0, 1, 1, 1],
               [0, 0, 1, 1],
               [1, 1, 1, 1],
               [0, 0, 0, 0]]
Output: 2
Explanation: Row 2 contains 4 1's (0-based indexing).'''

class Solution:

	def rowWithMax1s(self,arr):
	    maxi=0
	    index=-1
	    for i in range(len(arr)):
	        if arr[i].count(1)>maxi:
	            index=i
	            maxi=arr[i].count(1)
	    return index
