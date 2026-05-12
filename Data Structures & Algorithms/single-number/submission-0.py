class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = nums[0]
        for num in nums[1:]:
            cur = cur ^ num

        return cur