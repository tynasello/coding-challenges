'''
Count Connected Components

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] 
means that there is an edge between node a and node b in the graph.
The nodes are numbered from 0 to n - 1.
Return the total number of connected components in that graph.
'''

# DFS O(n+m)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        numComponents = 0

        visited = [0] * n
        
        for start in range(n):
            if not visited[start]:
                visited[start] = 1
                numComponents += 1
                stack = [start]
                while stack:
                    u = stack.pop()
                    for v in adjList[u]:
                        if not visited[v]:
                            visited[v] = 1
                            stack.append(v)

        return numComponents