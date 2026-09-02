class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        topK = []
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for key,value in count.items():
            bucket[value].append(key)
        
        for i in range(len(nums),0,-1):
            
            for n in bucket[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK
                
        
        
        


