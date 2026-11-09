class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        buyI = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[buyI]:
                profit = prices[i] - prices[buyI]
                max_profit = max(max_profit,profit)
            else:
                buyI = i

        return max_profit






        