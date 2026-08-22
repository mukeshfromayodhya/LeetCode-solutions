class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        profit = 0
        for i in range(0,len(prices)):
            if cheap > prices[i]:
                cheap = prices[i]
            current_profit = prices[i] - cheap
            profit = max(current_profit, profit)
            

        return profit