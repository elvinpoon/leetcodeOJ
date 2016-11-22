class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """        
        path = [[0] * n] * m
        if m==n and n == 1:
            return 0
        for i in range(1,len(path[0])):
            path[0][i] = 1
        if len(path) == 1:
            return path[0][len(path[0]) - 1]
        for i in range(1,len(path)):
            path[i][0] = 1
        if len(path[0]) == 1:
            return path[len(path)-1][0]

        for i in range(1,len(path)):
            for j in range(1,len(path[0])):
                path[i][j] = path[i-1][j]+path[i][j-1]

        return path[i][j]
m = Solution()
print m.uniquePaths(2,3)
print m.uniquePaths(1,3)
print m.uniquePaths(3,1)
print m.uniquePaths(3,3)
