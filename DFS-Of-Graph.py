'''Given a connected undirected graph containing V vertices represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Search (DFS) traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list, and return a list containing the DFS traversal of the graph.

Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]
Output: [0, 2, 4, 3, 1]
Explanation: Starting from 0, the DFS traversal proceeds as follows:
Visit 0 → Output: 0 
Visit 2 (the first neighbor of 0) → Output: 0, 2 
Visit 4 (the first neighbor of 2) → Output: 0, 2, 4 
Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3 
Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1

Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
Output: [0, 1, 2, 3, 4]

1 ≤ V = adj.size() ≤ 104
1 ≤ adj[i][j] ≤ 104'''

class Solution:

    def dfs(self, adj):
        visited=[False]*(len(adj)+1)
        start=0
        ans=[start]
        visited[start]=True
        self.helper(adj,visited,ans,start)
        return ans 
    def helper(self, adj, visited,ans,start):
        for i in adj[start]:
            if not visited[i]:
                ans.append(i)
                visited[i]=True
                self.helper(adj,visited,ans,i)

