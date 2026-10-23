class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0 , len(nums) - 1
        res = nums[0]

        while left<=right:
            #checks case where the list is already in order, and if not picks the left most value to be the smallest each time as ascending is left to right 
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                break

            mid = (left+right) // 2
            res = min(res, nums[mid]) #sets the minimum result to the smallest number 

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return res
