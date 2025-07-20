'''You are given an adjacency list, adj of Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Input: adj[][] = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], src=0
Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
 
Input: adj[][]= [[3], [3], [], [0, 1]], src=3
Output: [1, 1, -1, 0]

Input: adj[][]= [[], [], [], [4], [3], [], []], src=1
Output: [-1, 0, -1, -1, -1, -1, -1] 

1<=adj.size()<=104
0<=edges<=adj.size()-1'''


class Solution:
    def shortestPath(self, adj, src):
        
        from collections import deque
        dist=[-1]*len(adj)
        qu=deque([src])
        dist[src]=0
        
        while qu:
            curr=qu.popleft()
            
            for neighbor in adj[curr]:
                if dist[neighbor]==-1:
                    dist[neighbor]=dist[curr]+1
                    qu.append(neighbor)
                    
        return dist
