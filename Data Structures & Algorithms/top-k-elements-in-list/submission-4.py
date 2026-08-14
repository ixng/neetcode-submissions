class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        topK = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)


        for num in count:
            bucket[count[num]].append(num)
        
        for i in reversed(range(len(bucket))):
            
            if bucket[i] != None and len(topK) != k:
                topK.extend(bucket[i])
    
            if len(topK) == k:
                return topK
        
        return topK