class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            cur = matchsticks[i]
            for j in range(4):
                if sides[j] + cur <= target:
                    sides[j] += cur
                    if dfs(i+1):
                        return True
                    sides[j] -= cur
                
                if sides[j] == 0:
                    break
                
            return False
        
        return dfs(0)
        

