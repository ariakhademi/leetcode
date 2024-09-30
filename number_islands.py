"""
Given an m x n 2D binary grid grid which represents
a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by 
connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        nrows, ncols = len(grid), len(grid[0])

        if not grid:
            return 0

        def dfs(i,j):
            if i < 0 or i >= nrows or j < 0 or j >= ncols or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        nislands = 0

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    nislands += 1
                    dfs(i,j)

        return nislands 
        