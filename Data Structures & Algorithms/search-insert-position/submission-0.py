import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx