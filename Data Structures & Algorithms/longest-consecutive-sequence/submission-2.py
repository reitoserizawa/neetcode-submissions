class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxStreak = 0

        for n in nums:
            if not n-1 in nums:
                cur = n
                curStreak = 1
                while cur+1 in nums:
                    cur += 1
                    curStreak += 1
                maxStreak = max(maxStreak, curStreak)
        return maxStreak


        