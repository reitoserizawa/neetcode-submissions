class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, cur): 
            if i == len(nums):
                return cur
                     
            include = dfs(i+1, cur^nums[i])
            exclude = dfs(i+1, cur)
            return include + exclude

        return dfs(0, 0)
