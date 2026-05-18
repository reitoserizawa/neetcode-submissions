class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = None
        c1 = c2 = 0
        for n in nums:
            if n1 == n:
                c1 += 1
            elif n2 == n:
                c2 += 1
            elif c1 == 0:
                n1 = n
                c1 = 1
            elif c2 == 0:
                n2 = n
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        res = []
        for n in [n1, n2]:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res