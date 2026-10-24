class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        threshold = math.floor(len(nums)/2)
        for num in count:
            if count[num] > threshold:
                return num 