class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_streak = 0

        for num in set_nums:
            if num-1 not in set_nums:
                cur_num = num
                streak = 1
                while cur_num+1 in set_nums:
                    cur_num += 1
                    streak += 1
                max_streak = max(max_streak, streak)

        return max_streak