'''Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell. The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1. There should be atleast one 1 in the grid.

Input: grid = [[0,1,1,0], [1,1,0,0], [0,0,1,1]]
Output:  [[1,0,0,1], [0,0,1,1], [1,1,0,0]]

Input: grid = [[1,0,1], [1,1,0], [1,0,0]]
Output: [[0,1,0], [0,0,1], [0,1,2]]
Explanation: The grid is-
1 0 1
1 1 0
1 0 0
- 0's at (0,1), (1,2), (2,1) and (2,2) are at a  distance of 1, 1, 1 and 2 from 1's at (0,0), (0,2), (2,0) and (1,1) respectively.
 
1 ≤ n, m ≤ 500'''

class Solution:

	def nearest(self, grid):
	    from collections import deque
	    dist=[[-1]*len(grid[0]) for _ in range (len(grid))]
	    qu=deque([])
	    dirc=[(0,1),(0,-1),(-1,0),(1,0)]	    
	    for i in range(len(grid)):
	        for j in range(len(grid[0])):
	            if grid[i][j]==1:
	                dist[i][j]=0
	                qu.append((i,j))
	               
	    while qu:
	        row,col=qu.popleft()

	        for pos in dirc:
	            rowx=row+pos[0]
	            coly=col+pos[1]
	            
	            if rowx>-1 and rowx<len(grid) and coly>-1 and coly<len(grid[0]) and dist[rowx][coly]==-1:
	                    dist[rowx][coly]=dist[row][col]+1
	                    qu.append((rowx,coly))
	    
	    return dist
	    
