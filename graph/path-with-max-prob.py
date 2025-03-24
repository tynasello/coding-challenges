'''
Leetcode 1514, Path with Maximum Probability

1514. Path with Maximum Probability
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge 
list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a 
probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to 
go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it 
differs from the correct answer by at most 1e-5.
'''

# Djikstras O((m+n)logn)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob = [0] * n # prob[i] = max prob from start_node to node i
        prob[start_node] = 1

        adjList = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adjList[u].append([v, p])
            adjList[v].append([u, p])

        maxHeap = [[-1, start_node]] # [prob from start_node to u, u]
        maxFound = {} # maxFound[i] = 1 if the max prob from start_node to i is found, else 0

        while maxHeap:
            pu, u = heapq.heappop(maxHeap)
            pu *= -1

            if u in maxFound:
                continue
            else:
                maxFound[u] = True

            if u == end_node:
                return prob[u]

            for v, pv in adjList[u]:
                if v in maxFound:
                    continue
                if pu * pv > prob[v]:
                    prob[v] = pu * pv
                    heapq.heappush(maxHeap, [prob[v] * -1, v])

        return 0

# Bellman-ford O(n + mn)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob = [0] * n # prob[i] = max prob from start_node to node i
        prob[start_node] = 1

        for _ in range(n-1):
            updated = False
            for i in range(len(edges)):
                u, v = edges[i]
                p = succProb[i]
                if prob[u] * p > prob[v]:
                    prob[v] = prob[u] * p
                    updated = True
                if prob[v] * p > prob[u]:
                    prob[u] = prob[v] * p
                    updated = True
                
            if not updated:
                break

        return prob[end_node]

