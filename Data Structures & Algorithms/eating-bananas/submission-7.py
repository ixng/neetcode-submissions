class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxRate = max(piles)
        bestRate = maxRate
        hours = 0
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l+r) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b/mid)
                
            if hours <= h:
                bestRate = min(bestRate,mid)
                r = mid - 1
            else:
                l = mid + 1

            
        return bestRate

