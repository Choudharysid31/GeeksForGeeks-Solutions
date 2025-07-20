'''Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y). 
Note: You can only move left, right, up and down, and only through cells that contain 1.

Input:
N=3, M=4
A=[[1,0,0,0], 
   [1,1,0,1],
   [0,1,1,1]]
X=2, Y=3 
Output:
5
Explanation:
The shortest path is as follows:
(0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(2,3).

Input:
N=3, M=4
A=[[1,1,1,1],
   [0,0,0,1],
   [0,0,0,1]]
X=0, Y=3
Output:
3
Explanation:
The shortest path is as follows:
(0,0)->(0,1)->(0,2)->(0,3).

1 <= N,M <= 250
0 <= X < N
0 <= Y < M
0 <= A[i][j] <= 1'''

class Solution:
    def shortestDistance(self,N,M,A,X,Y):


        if A[0][0]==0 or A[X][Y]==0:
            return -1
        
        dirc=[(0,-1),(0,1),(1,0),(-1,0)]
        
        from collections import deque

        A[0][0]=0
        qu=deque([(0,0,0)])

        while qu:
            row,col,step=qu.popleft()

            if [row,col]==[X,Y]:
                
                return step
                
            for pos in dirc:
                rowx=row+pos[0]
                coly=col+pos[1]
                
                if rowx>-1 and rowx<N and coly>-1 and coly<M and A[rowx][coly]:
                    qu.append((rowx,coly,step+1))
                    A[rowx][coly]=0
        return -1
