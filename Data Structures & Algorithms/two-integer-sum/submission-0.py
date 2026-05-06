class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in seen:
                return [seen[wanted], i]
            else:
                seen[nums[i]] = i