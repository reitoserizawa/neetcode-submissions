class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)

        target = len(nums)//3
        res = []

        for n, cnt in cnt.items():
            if cnt > target:
                res.append(n)

        return res