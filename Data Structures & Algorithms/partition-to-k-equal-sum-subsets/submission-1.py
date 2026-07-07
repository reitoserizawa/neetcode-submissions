class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        nums.sort(reverse=True)
        target = int(sum(nums)/k)
        used = [False] * len(nums)

        def dfs(i, cur, completed):
            if completed == k-1:
                return True
            
            if cur == target:
                return dfs(0, 0, completed+1)
            
            for j in range(i, len(nums)):
                if used[j]:
                    continue
                
                if cur+nums[j] > target:
                    continue

                used[j] = True    
                if dfs(j+1, cur+nums[j], completed):
                    return True
                used[j] = False
            
            return False
            
        return dfs(0, 0, 0)