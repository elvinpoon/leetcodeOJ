class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        path = grid
        for i in range(1,len(grid[0])):
            path[0][i] += path[0][i-1]
        if len(grid) == 1:
            return path[0][len(grid[0]) - 1]
        for i in range(1,len(grid)):
            path[i][0] += path[i-1][0]
        if len(grid[0]) == 1:
            return path[len(grid)-1][0]

        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                path[i][j] += min(path[i-1][j],path[i][j-1])

        return path[i][j]

m = Solution()
print m.minPathSum([[1,2,3],[3,4,5]])
print m.minPathSum([[1,2,3]])
print m.minPathSum([[1],[3],[5]])
print m.minPathSum([[1]])