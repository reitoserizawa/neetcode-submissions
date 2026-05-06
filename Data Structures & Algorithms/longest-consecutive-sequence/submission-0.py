class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num-1 not in num_set:
                cur_num = num
                cur_streak = 1
                while cur_num+1 in num_set:
                    cur_num += 1
                    cur_streak += 1
                longest_streak = max(longest_streak, cur_streak)
        
        return longest_streak