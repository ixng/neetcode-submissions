class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 
        

        while l <= r:
            mid = (l+r) // 2
            
            if target == nums[mid]:
                return mid
            # if left sorted
            if nums[l] <= nums[mid]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1

    