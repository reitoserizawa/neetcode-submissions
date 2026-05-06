class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            summ = numbers[l] + numbers[r]
            if target == summ:
                return [l+1, r+1]
            if target < summ:
                r -= 1
            else:
                l += 1