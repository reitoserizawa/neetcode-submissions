class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        arr = []

        for i, n in enumerate(nums):
            if n in seen:
                arr.append(i)
            seen.add(n)
        
        while arr:
            i = arr.pop()
            nums.pop(i)
        
        return len(nums)