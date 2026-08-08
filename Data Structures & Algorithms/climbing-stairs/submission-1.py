class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * n

        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            
            memo[i] = dfs(i+1) + dfs(i+2) if memo[i] is None else memo[i]

            return memo[i]


        return dfs(0)