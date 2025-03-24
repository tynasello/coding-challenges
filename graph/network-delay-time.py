'''
Leetcode 743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of 
travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the 
target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n 
nodes to receive the signal. If it is impossible for all the n nodes to receive the signal,
return -1.
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adjList[u].append([v, w])

        dist = [math.inf] * (n + 1) # dist[i] = min dist from k to node i
        dist[0] = 0
        dist[k] = 0

        minFound = set()

        minHeap = [[0, k]]

        while minHeap:
            wu, u = heapq.heappop(minHeap)
            if u in minFound:
                continue
            minFound.add(u)

            for v, wv in adjList[u]:
                if v in minFound:
                    continue
                if wu + wv < dist[v]:
                    dist[v] = wu + wv
                    heapq.heappush(minHeap, [dist[v], v])

        return max(dist) if len(minFound) == n else -1