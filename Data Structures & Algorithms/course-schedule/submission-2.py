class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:            
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)

        visiting = set()
        visited = set()

        def dfs(cur):            
            if cur in visited:
                return True
            
            if cur in visiting:
                return False
            
            visiting.add(cur)
            for child in adj[cur]:
                if not dfs(child):
                    return False
            visiting.remove(cur)
            visited.add(cur)
        
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True



            
            

        