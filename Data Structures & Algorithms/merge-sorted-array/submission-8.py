class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        r = 0
        k = 0
        left = nums1[:m]
        
        while l < len(left) and r < len(nums2):
            if left[l] <= nums2[r]:
                nums1[k] = left[l]
                l+=1
                k+=1
            else:
                nums1[k] = nums2[r]
                r+=1
                k+=1
        
        while l < len(left):
            nums1[k] = left[l]
            l+=1
            k+=1

        while r < len(nums2):
            nums1[k] = nums2[r]
            r+=1
            k+=1

