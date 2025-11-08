'''You are given a matrix mat[][] of size n x m, where each of its cells contains some coins. Count the number of ways to collect exactly k coins while moving from the top left cell of the matrix to the bottom right cell. From a cell (i, j), you can only move to cell (i+1, j) or (i, j+1).
Input: k = 12, mat[] = [[1, 2, 3],
                      [4, 6, 5],
                      [3, 2, 1]]
Output: 2
Explanation: There are 2 possible paths with exactly 12 coins, (1 + 2 + 6 + 2 + 1) and (1 + 2 + 3 + 5 + 1).

Input: k = 16, mat[] = [[1, 2, 3], 
                      [4, 6, 5], 
                      [9, 8, 7]]
Output: 0'''

class Solution:
    def numberOfPath(self, mat, k):
        dp=[[[(0) for _ in range(k+1)] for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        if mat[0][0]>k:
            return 0
        dp[0][0][mat[0][0]]=1
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for m in range(k+1):
                    
                        if (i+1<len(mat)) and (mat[i+1][j]+m)<=k:
                            dp[i+1][j][m+mat[i+1][j]]+=dp[i][j][m]
                        if (j+1<len(mat[0])) and (mat[i][j+1]+m<=k):
                            dp[i][j+1][m+mat[i][j+1]]+=dp[i][j][m]
                            
        
        return dp[-1][-1][-1]
