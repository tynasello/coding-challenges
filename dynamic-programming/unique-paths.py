'''
Leetcode 62, Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach 
the bottom-right corner
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * n for _ in range(m)]
        paths[0][0] = 1
        q = deque()
        q.append((0,0))

        while q:
            i, j = q.popleft()
            if i + 1 < m:
                if not paths[i+1][j]:
                    q.append((i+1, j))
                paths[i+1][j] += paths[i][j]
            if j + 1 < n:
                if not paths[i][j+1]:
                    q.append((i, j+1))
                paths[i][j+1] += paths[i][j]

        return paths[m-1][n-1]
    
    # Bottom up DP
    # def uniquePaths(self, m: int, n: int) -> int:
    #     paths = [[0] * n for _ in range(m)]

    #     for i in range(m):
    #         paths[i][n-1] = 1
    #     for i in range(n):
    #         paths[m-1][i] = 1

    #     for i in range(m-2, -1, -1):
    #         for j in range(n-2, -1, -1):
    #             paths[i][j] = paths[i+1][j] + paths[i][j+1]
    
    #     return paths[0][0]

    # Math solution
    # def uniquePaths(self, m: int, n: int) -> int:
    #     a = m-1 + n-1
    #     k = m-1
    #     # a choose k
    #     return factorial(a) // (factorial(a-k) * factorial(k))

                