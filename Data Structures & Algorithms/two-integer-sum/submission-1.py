class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i, n in enumerate(nums):
            cur = target - n
            if cur in seen:
                return [seen[cur], i]
            seen[n] = i
        
        return []