class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        r = 0
        k = 0
        left = nums1[:m]
        right = nums2
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                nums1[k] = left[l]
                l+=1
                k+=1
            else:
                nums1[k] = right[r]
                r+=1
                k+=1
        
        while l < len(left):
            nums1[k] = left[l]
            l+=1
            k+=1

        while r < len(right):
            nums1[k] = right[r]
            r+=1
            k+=1

