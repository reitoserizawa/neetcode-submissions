class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        
        if len(a) > len(b):
            a, b = b, a
        
        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(a)-1
        while True:
            i = (l+r) // 2
            j = half - i - 2

            leftA = a[i] if i >= 0 else float('-inf')
            rightA = a[i+1] if (i+1) < len(a) else float('inf')
            leftB = b[j] if j >= 0 else float('-inf')
            rightB = b[j+1] if (j+1) < len(b) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            else:
                if leftA > rightB:
                    r = i -1
                else:
                    l = i + 1