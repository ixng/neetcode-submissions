class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length - 1

        while left <= right:
            mid = (left + right) // 2 
            mid_value = nums[mid]
            right_value = nums[right] 
            left_value = nums[left]
            
            if left == right:
                return nums[right]

            if mid_value < right_value and mid_value < left_value:
                left += 1
                right -=1 
            elif right_value < left_value:
                if mid_value <= right_value:
                    left = mid
                else:
                    left = mid + 1
            elif right_value > left_value:
                if mid_value <= left_value:
                    right = mid
                else:
                    right = mid - 1


        
