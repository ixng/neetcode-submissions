class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        topK = []

        for num in nums:
            count[num] = 1 + count.get(num,0)


        for num, count in count.items():
            bucket[count].append(num)
        
        for i in range(len(bucket) - 1, 0, -1):
            
            if bucket[i] != None and len(topK) != k:
                topK.extend(bucket[i])
    
            if len(topK) == k:
                return topK
        
        return topK