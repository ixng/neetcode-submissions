class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      arr = [(num,i) for i, num in enumerate(nums)]
      
      arr.sort()
      r = len(arr) - 1
      l = 0
      while l<r:
        sum = arr[r][0] + arr[l][0]
        if sum < target:
            l+=1
        elif sum > target:
            r-=1
        else:
            return sorted([arr[l][1], arr[r][1]])

      return []
            
            
    
      
