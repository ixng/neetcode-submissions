class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in rem:
                return sorted([rem[diff],i])
            rem[nums[i]] = i

        return []