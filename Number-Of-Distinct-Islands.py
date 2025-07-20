'''Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).

Input: grid[][] = {{1, 1, 0, 0, 0},
                   {1, 1, 0, 0, 0},
                   {0, 0, 0, 1, 1},
                   {0, 0, 0, 1, 1}}
Output: 1
Explanation: We have 2 equal islands, so we have only 1 distinct island.


Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output: 3
Explanation: We have 4 islands, but 2 of them are equal, So we have 3 distinct islands.

Expected Time Complexity: O(n * m)
Expected Space Complexity: O(n * m)'''


import sys
from typing import List
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]):
        
        shape=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    shape.add(self.bfs(grid,i,j))
        return len(shape)
    
    def bfs(self,grid,start,end):
        
        shaper=[]
        dirc=[(0,1),(0,-1),(-1,0),(1,0)]
        qu=deque([(start,end)])
        grid[start][end]=0
        
        while qu:
            row,col=qu.popleft()
            
            for pos in dirc:
                rowx=pos[0]+row
                coly=pos[1]+col
                
                if rowx>-1 and rowx<len(grid) and coly>-1 and coly<len(grid[0]) and grid[rowx][coly]==1:
                    qu.append((rowx,coly))
                    grid[rowx][coly]=0
                    shaper.append((start-rowx,end-coly))
                    
        return tuple(shaper)
