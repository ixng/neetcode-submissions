class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        buyI = 0
        currProf = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[buyI]:
                profit = prices[i] - prices[buyI]
                currProf = max(currProf,profit)
            else:
                buyI = i
        return currProf 
            