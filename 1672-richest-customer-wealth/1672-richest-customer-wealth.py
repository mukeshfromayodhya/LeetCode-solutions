class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts[:]:
            total_wealth = sum(i)
            max_wealth = max(max_wealth,total_wealth)
        return max_wealth