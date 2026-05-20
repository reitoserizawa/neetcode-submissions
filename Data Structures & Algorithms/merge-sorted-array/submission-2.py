class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = m+n-1

        i2 = n-1

        while i >= 0 and i2 >= 0:
            if nums1[i] > nums2[i2]:
                nums1[j] = nums1[i]
                i -= 1
            else:
                nums1[j] = nums2[i2]
                i2 -= 1
            j -= 1
        
        while i2 >= 0:
            nums1[j] = nums2[i2]
            i2 -= 1
            j -= 1