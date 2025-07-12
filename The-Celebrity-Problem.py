'''A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] (n*n) is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Input: mat[][] = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1st person. Therefore, 1 is the celebrity person. 

Input: mat[][] = [[1, 1], [1, 1]]
Output: -1
Explanation: Since both the people at the party know each other. Hence none of them is a celebrity person.

Input: mat[][] = [[1]]
Output: 0

1 <= mat.size()<= 1000
0 <= mat[i][j]<= 1
mat[i][i] == 1'''

class Solution:
    def celebrity(self, mat):
        
        idx=-1
        for i in range(len(mat)):
            count=0
            for j in range(len(mat)):
                if mat[i][j]==1:
                    count+=1
                if count>1:
                    break
            if count==1:
                idx=i
                break
        if idx==-1:
            return -1
            
        for row in range(len(mat)):
            if mat[row][idx]!=1:
                return -1
                
        return idx
