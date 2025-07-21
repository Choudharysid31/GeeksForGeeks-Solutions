'''Given a Graph with V vertices (Numbered from 0 to V-1) and E edges. Check whether the graph is bipartite or not.
A bipartite graph can be colored with two colors such that no two adjacent vertices share the same color. This means we can divide the graph’s vertices into two distinct sets where:
All edges connect vertices from one set to vertices in the other set.
No edges exist between vertices within the same set.

Input: V = 3, edges[][] = [[0, 1], [1,2]]
Bipartite-Graph
Output: true

Input: V = 4, edges[][] = [[0, 3], [1, 2], [3, 2], [0, 2]]
Output: false 
Explanation: The given graph cannot be colored in two colors such that color of adjacent vertices differs. 

1 ≤ V ≤ 2 * 105
1 ≤ edges.size() ≤ 105
1 ≤ edges[i][j] ≤ 105'''


class Solution:
    def isBipartite(self, V, edges):
        col=[-1]*V
        adj=[[]*V for _ in range(V)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        for i in range(V):
            if col[i]==-1 and not self.bfs(adj,col,i):
                return False
                
        return True
        
        
    def bfs(self,adj,col,start):
        from collections import deque
        qu=deque([start])
        col[start]=0
        while qu:
                
            curr=qu.popleft()
                
            for neighbor in adj[curr]:
                if col[neighbor]==-1:
                    col[neighbor]=1-col[curr]
                    qu.append(neighbor)
                elif col[neighbor]==col[curr]:
                    return False
        return True
