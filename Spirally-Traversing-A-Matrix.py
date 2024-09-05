'''You are given a rectangular matrix, and your task is to return an array while traversing the matrix in spiral form.

Input: matrix[][] = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15,16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

Input: matrix[][] = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
Explanation: Applying same technique as shown above, output for the 2nd testcase will be 1 2 3 4 8 12 11 10 9 5 6 7.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(n2)'''
class Solution:
    def spirallyTraverse(self, matrix):
        ans=[]
        total=(len(matrix))*len(matrix[0])
        left=-1
        right=len(matrix[0])
        bottom=len(matrix)
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
        return ans
        
