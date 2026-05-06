class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        N = len(words)
        for word in words:
            for c in word:
                adj[c] = set()
                
        for i in range(N-1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        

        visited = {}
        res = []
        def dfs(cur):
            if cur in visited:
                return visited[cur]
            
            visited[cur] = True
            for nei in adj[cur]:
                if dfs(nei):
                    return True
            visited[cur] = False
            res.append(cur)
        
        for c in adj:
            if dfs(c):
                return ""
        return ''.join(res[::-1])

