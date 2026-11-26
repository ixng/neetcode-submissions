class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        zeros = [] # hold the indexes of where the 0's are in nums1

        
        nums1[m:] = nums2[:n]
        nums1.sort()
