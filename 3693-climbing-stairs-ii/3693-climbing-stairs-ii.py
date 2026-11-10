class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(max(0,i-3),i):
                jump = i -j
                total = dp[j] + costs[i - 1] + jump ** 2
                dp[i] = min(dp[i], total)
        return dp[n]