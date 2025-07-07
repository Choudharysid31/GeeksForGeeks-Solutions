''' Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation: 
1 -> 2 -> 0 -> 1 is a cycle.

Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false

1 ≤ V ≤ 105
1 ≤ E = edges.size() ≤ 105'''

class Solution:

	def isCycle(self, V, edges):
	    visited = [-1] * V
	    adj=[[] for _ in range (V)]
	    for u, v in edges:
	        
	        adj[u].append(v)
            adj[v].append(u)
            
		def bfs(start):
		    from collections import deque
		    visited[start]=1
		    qu=deque()
		    qu.append((start,-1))
		    while qu:
		        curr,parent=qu.popleft()
		        for neighbour in adj[curr]:
		            if visited[neighbour]==-1:
		                visited[neighbour]=1
		                qu.append((neighbour,curr))
		            elif neighbour!=parent:
		                    return True
		    return False
		
		for i in range(V):
		    if visited[i]==-1 and bfs(i):
		        return True
		return False

