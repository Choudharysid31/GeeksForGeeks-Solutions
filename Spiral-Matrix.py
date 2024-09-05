'''Given a matrix of size N x M. You have to find the Kth element which will obtain while traversing the matrix spirally starting from the top-left corner of the matrix.

Input: N = 3, M = 3, K = 4
A[] = {{1, 2, 3}, 
       {4, 5, 6}, 
       {7, 8, 9}}
Output: 6
Explanation: Spiral traversal of matrix: {1, 2, 3, 6, 9, 8, 7, 4, 5}. Fourth element is 6.

Input: N = 2, M = 2, K = 2 
A[] = {{1, 2},
       {3, 4}} 
Output: 2
Explanation: Spiral traversal of matrix: {1, 2, 4, 3}. Second element is 2.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)'''

class Solution:
    def findK(self, matrix, n, m, k):
        ans=[]
        total=0
        left=-1
        right=len(matrix[0])
        bottom=len(matrix)
        upper=-1
        i=0 
        j=0
        move='RIGHT'
        while total<=k:
            if move =='RIGHT':
                i=upper+1
                j=left+1
                while j<right:
                    ans.append(matrix[i][j])
                    j+=1
                    total+=1
                move='DOWN'
                upper+=1
            elif move=='DOWN':
                j=right-1
                i=upper+1
                while i<bottom:
                    ans.append(matrix[i][j])
                    i+=1
                    total+=1
                move='LEFT'
                right-=1
            elif move=='LEFT':
                j=right-1
                i=bottom-1
                while j>left:
                    ans.append(matrix[i][j])
                    j-=1
                    total+=1
                move='UP'
                bottom-=1
            
            else:
                j=left+1
                i=bottom-1
                while i>upper:
                    ans.append(matrix[i][j])
                    i-=1
                    total+=1
                move='RIGHT'
                left+=1
                
        return ans[k-1]
