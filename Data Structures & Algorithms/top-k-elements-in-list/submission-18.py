class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        counts = {}
        res = []

        for num in nums:
            counts[num] = counts.get(num,0) + 1

        arr = []
        for num, count in counts.items():
            arr.append([count,num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res