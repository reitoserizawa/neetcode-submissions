class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, used):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for j in range(len(nums)):
                if j not in used:
                    used.add(j)
                    cur.append(nums[j])

                    dfs(cur, used)

                    used.remove(j)
                    cur.pop()
        
        dfs([], set())
        return res