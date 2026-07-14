class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        memo = {}
        def dfs(cur, target):
            if cur == target:
                return True
            
            if (cur, target) in memo:
                return memo[(cur, target)]
            
            for child in adj[cur]:
                if dfs(child, target):
                    memo[(cur, target)] = True
                    return memo[(cur, target)]
            memo[(cur, target)] = False
            return memo[(cur, target)]
        
        res = []
        for a, b in queries:
            if dfs(a, b):
                res.append(True)
            else:
                res.append(False)
        
        return res