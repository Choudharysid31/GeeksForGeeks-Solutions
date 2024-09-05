'''Given a matrix as 2D array. Find the reverse spiral traversal of the matrix. 

Input: R = 3, C = 3
  a = {{9, 8, 7},
       {6, 5, 4},
       {3, 2, 1}}
Output: 5 6 3 2 1 4 7 8 9
Explanation: Spiral form of the matrix in reverse order starts from the centre and goes outward.

Input: R = 4, C = 4 
  a = {{1, 2, 3, 4},
       {5, 6, 7, 8},
       {9, 10, 11, 12}, 
       {13, 14, 15, 16}}
Output: 10 11 7 6 5 9 13 14 15 16 12 8 4 3 2 1

Expected Time Complexity: O(R*C)
Expected Auxiliary Space: O(R*C)'''
class Solution:
	def reverseSpiral(self, R, C, matrix):
		ans=[]
        total=R*C
        left=-1
        right=C
        bottom=R
        upper=-1
        i=0 
        j=0
        move='RIGHT'
        while total:
            if move =='RIGHT':
                i=upper+1
                j=left+1
                while j<right:
                    ans.append(matrix[i][j])
                    j+=1
                    total-=1
                move='DOWN'
                upper+=1
            elif move=='DOWN':
                j=right-1
                i=upper+1
                while i<bottom:
                    ans.append(matrix[i][j])
                    i+=1
                    total-=1
                move='LEFT'
                right-=1
            elif move=='LEFT':
                j=right-1
                i=bottom-1
                while j>left:
                    ans.append(matrix[i][j])
                    j-=1
                    total-=1
                move='UP'
                bottom-=1
            
            else:
                j=left+1
                i=bottom-1
                while i>upper:
                    ans.append(matrix[i][j])
                    i-=1
                    total-=1
                move='RIGHT'
                left+=1
        return ans[::-1]
