'''Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Search (BFS) traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]
Output: [0, 2, 3, 1, 4]

Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
Output: [0, 1, 2, 3, 4]
Explanation: Starting from 0, the BFS traversal proceeds as follows: 

1 ≤ V = adj.size() ≤ 104
1 ≤ adj[i][j] ≤ 104'''

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n=len(adj)
        visited=[-1]*n
        start=0
        visited[start]=1
        ans=[]
        from collections import deque
        qu=deque([start])
        while qu:
            start=qu.popleft()
            ans.append(start)
            for neighbour in adj[start]:
                if visited[neighbour]==-1:
                    qu.append(neighbour)
                    visited[neighbour]=1
        return ans
