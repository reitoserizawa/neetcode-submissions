class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        min_i = 0

        while l <= r:
            mid = (l+r)//2
            if l == r:
                min_i = l
                break
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        if min_i == 0:
            l, r = 0, len(nums)-1
        elif nums[min_i] <= target <= nums[-1]:
            l, r = min_i, len(nums)-1
        else:
            l, r = 0, min_i - 1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1