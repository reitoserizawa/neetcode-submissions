class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        res = []
        visiting = set()
        visited = set()

        def dfs(i):
            if i in visited:
                return True

            if i in visiting:
                return False

            visiting.add(i)
            for child in adj[i]:
                if not dfs(child):
                    return False
            visiting.remove(i)
            visited.add(i)
            res.append(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res