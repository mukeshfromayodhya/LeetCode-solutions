class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        # Step 1: Precompute semi-palindrome costs
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best = float('inf')

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for r in range(d):
                        left = i + r
                        right = i + r + (groups - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # Step 2: Partition DP
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):

                    dp[end][parts] = min(
                        dp[end][parts],
                        dp[start][parts - 1] + cost[start][end - 1]
                    )

        return dp[n][k]