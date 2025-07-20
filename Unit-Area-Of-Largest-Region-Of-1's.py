'''Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s. Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).

Input: grid = {{1,1,1,0},{0,0,1,0},{0,0,0,1}}
Output: 5
Explanation: The grid is-
1 1 1 0
0 0 1 0
0 0 0 1
The largest region of 1's is 5

Input: grid = {{0,1}}
Output: 1

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)'''

class Solution:
    def bfs(self,grid,startr,startc):
        
        from collections import deque
        grid[startr][startc]=0
        dirc=[(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,1),(1,-1)]
        qu=deque([(startr,startc)])
        leni=1
        while qu:
            row,col=qu.popleft()
            
            for pos in dirc:
                
                rowx=row+pos[0]
                coly=col+pos[1]
                
                if rowx > -1 and rowx<(len(grid)) and coly>-1 and coly<(len(grid[0])) and grid[rowx][coly]==1:
                    qu.append((rowx,coly))
                    grid[rowx][coly]=0
                    leni+=1
        return leni
                
	def findMaxArea(self, grid):

	    ans=0
	    
	    for i in range(len(grid)):
	        for j in range(len(grid[0])):
	            if grid[i][j]==1:
	                ans=max(ans,self.bfs(grid,i,j))
	                
	    return ans
