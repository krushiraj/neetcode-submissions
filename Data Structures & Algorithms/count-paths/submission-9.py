class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memory = [[-1 for j in range(n)] for i in range(m)]

        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if memory[i][j] == -1:
                memory[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memory[i][j]

        return dfs(0, 0)