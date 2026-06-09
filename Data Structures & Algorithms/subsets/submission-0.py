class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return

            # include
            cur.append(nums[i])
            backtrack(i+1, cur)
            # skip
            cur.pop()
            backtrack(i+1, cur)
        
        backtrack(0, [])
        return res