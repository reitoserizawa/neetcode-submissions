class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # Left pointer - Buy day
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r  # Shift the buy day to the current day

        return max_profit