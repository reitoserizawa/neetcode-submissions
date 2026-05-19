class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix = 0

        seen = defaultdict(int)
        seen[0] = 1

        for n in nums:
            prefix += n
            if prefix-k in seen:
                cnt += seen[prefix-k]
            seen[prefix] += 1
        
        return cnt