class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            new_dp = [0] * k
            remainder = num % k
            new_dp[remainder] += 1

            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * remainder) % k
                    new_dp[new_remainder] += dp[r]

            dp = new_dp

            for r in range(k):
                ans[r] += dp[r]

        return ans