'''Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.
Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Input: grid[][] = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]
Output: 4

Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'], ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
Output: 2

1 ≤ n, m ≤ 500
grid[i][j] = {'L', 'W'}'''

class Solution:
    def bfs(self,visited, grid, start):
        from collections import deque
        startr=start[0]
        startc=start[1]
        
        visited[startr][startc]=True
        
        hdir=[0,-1,1,1,-1,0,1,-1]
        vdir=[-1,-1,-1,0,0,1,1,1]
        qu=deque()
        qu.append((startr,startc))
        while qu:
            nx,ny=qu.popleft()
            for i in range(8):
                
                x=nx+hdir[i]
                y=ny+vdir[i]
                
                if (0<=x<len(grid)) and (0<=y<len(grid[0])) and (not visited[x][y]) and (grid[x][y]=="L"):
                    qu.append((x,y))
                    visited[x][y]=True
        
        
    def numIslands(self, grid):
        
        count=0
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        
        count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               if not visited[i][j] and grid[i][j]=="L":
                   self.bfs(visited,grid,(i,j))
                   count+=1
                   
        return count
