class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        rates = max(piles)
        bestRate = rates
        l = 1
        r = rates
    
        while l<=r:
            rate = (l+r) // 2
            hours = 0
            for bananas in piles:
                hours+= math.ceil(bananas/rate)
            
            if hours <= h:
                bestRate = min(bestRate, rate)
                r = rate - 1
            else:
                l = rate + 1
            
        return bestRate
