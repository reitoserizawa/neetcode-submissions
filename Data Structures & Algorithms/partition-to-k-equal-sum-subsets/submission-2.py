class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        nums.sort(reverse=True)
        buckets = [0] * k

        def dfs(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if buckets[j]+nums[i] <= target:
                    buckets[j] += nums[i]
                    if dfs(i+1):
                        return True
                    buckets[j] -= nums[i]
  
                if buckets[j] == 0:
                    break
            return False
            
        return dfs(0)