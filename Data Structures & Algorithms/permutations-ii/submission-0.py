class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(cur, visited):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and i-1 in visited:
                    continue
                if i not in visited:
                    cur.append(nums[i])
                    visited.add(i)
                    dfs(cur, visited)
                    cur.pop()
                    visited.remove(i)
        
        dfs([], set())
        return res