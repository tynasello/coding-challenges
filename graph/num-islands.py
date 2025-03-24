'''
Leetcode 100, Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    count += 1
                    q = deque()
                    q.append((i, j))
                    while (q):
                        a, b = q.popleft()
                        if a+1 < len(grid) and grid[a+1][b] == "1":
                            grid[a+1][b] = "0"
                            q.append((a+1, b))
                        if b+1 < len(grid[a]) and grid[a][b+1] == "1":
                            grid[a][b+1] = "0"
                            q.append((a, b+1))
                        if a-1 >= 0 and grid[a-1][b] == "1":
                            grid[a-1][b] = "0"
                            q.append((a-1, b))
                        if b-1 >= 0 and grid[a][b-1] == "1":
                            grid[a][b-1] = "0"
                            q.append((a, b-1))

        return count