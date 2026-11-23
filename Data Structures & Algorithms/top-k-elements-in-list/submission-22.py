class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for num,count in count.items():
            bucket[count].append(num)
        
        for i in range(len(bucket) - 1,0, -1):
            res.extend(bucket[i])
            if len(res) == k:
                return res
        