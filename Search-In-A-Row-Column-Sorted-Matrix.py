'''Given a 2D integer matrix mat[][] of size n x m, where every row and column is sorted in increasing order and a number x, the task is to find whether element x is present in the matrix.

Input: mat[][] = [[3, 30, 38],[20, 52, 54],[35, 60, 69]], x = 62
Output: false
Explanation: 62 is not present in the matrix, so output is false.

Input: mat[][] = [[18, 21, 27],[38, 55, 67]], x = 55
Output: true
Explanation: 55 is present in the matrix.'''

class Solution:
	def matSearch(self, mat, x):
		for i in range(len(mat)):
		    left=0
		    right=(len(mat[i]))-1
		    
		    while left<=right:
		        mid=left+(right-left)//2
		 
		        if mat[i][mid]==x:
		            return True
		        elif mat[i][mid]>x:
		            right-=1
		        
		        else:
		            left+=1
		return False
