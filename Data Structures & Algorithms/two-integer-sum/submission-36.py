class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      arr = {}
      for i, num in enumerate(nums):
        difference = target - num

        if difference in arr:
            return [arr[difference],i]
        else:
            arr[num] = i
      
      return []

    
      
