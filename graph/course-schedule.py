'''
Leetcode 207, Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for pr in prerequisites:
            adj[pr[1]].append(pr[0])

        comp = [0] * numCourses
        compNum = 1
        onPath = [0] * numCourses

        self.cycleExists = False

        def dfs(u):
            comp[u] = compNum
            onPath[u] = 1
            for v in adj[u]:                
                if not comp[v]:
                    dfs(v)
                elif onPath[v]:
                    self.cycleExists = True
            onPath[u] = 0
    
        for u in range(numCourses):
            if not comp[u]:
                dfs(u)
                compNum += 1
         
        return not self.cycleExists