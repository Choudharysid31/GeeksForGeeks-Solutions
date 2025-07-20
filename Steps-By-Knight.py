'''Given a square chessboard of size (n x n), the initial position and target postion of Knight are given. Find out the minimum steps a Knight will take to reach the target position.
The initial and the target position coordinates of Knight have been given according to 1-base indexing.

Input: n = 3, knightPos[] = [3, 3], targetPos[]= [1, 2]
Output: 1
Explanation: Knight takes 1 step to reach from 

Input: n = 6, knightPos[] = [4, 5],targetPos[] = [1, 1]
Output: 3
Explanation:Knight takes 3 step to reach from 
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).

1 <= n<= 1000
1 <= knightpos ≤ [x, y], targertpos[x, y] ≤  n'''

class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, n):
	    visited=[[False]*n for _ in range(n)]
	    dirc=[(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(-2,-1),(-2,1),(2,1)]
	    from collections import deque
	    startr=knightPos[0]-1
	    startc=knightPos[1]-1
	    visited[startr][startc]=True
	    qu=deque([(startr,startc,0)])
	    while qu:
	        row,col,step=qu.popleft()
	        if [row+1,col+1]==targetPos:
	            return step
	            
	        for pos in dirc:
	            
	            rowx=row+pos[0]
	            coly=col+pos[1]
	            
	            if rowx > -1 and rowx < n and coly > -1 and coly < n and not visited[rowx][coly]:
	                visited[rowx][coly]=True
	                qu.append((rowx,coly,step+1))    
	    return 0
