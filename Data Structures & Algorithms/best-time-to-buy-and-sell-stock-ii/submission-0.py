class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold = 0, -prices[0]

        for p in prices[1:]:
            prev_cash = cash
            cash = max(cash, hold+p)
            hold = max(hold, prev_cash-p)

        return cash