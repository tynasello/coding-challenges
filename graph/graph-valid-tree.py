'''
Leetcode 261 Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.
'''

from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [0] * n

        adjlist = [[] for _ in range(n)]
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)

        q = deque()
        q.append([0, -1]) # node and parent

        while q:
            node, parent = q.popleft()
            if visited[node]:
                return False
            visited[node] = 1
            
            for b in adjlist[node]:
                if b != parent:
                    q.append([b, node])
        
        for v in visited:
            if not v:
                return False
        return True
            