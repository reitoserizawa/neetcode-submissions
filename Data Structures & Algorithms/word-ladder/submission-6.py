class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        seen = {beginWord}
        q = deque([(beginWord, 1)])
        
        while q:
            w, cnt = q.popleft()
            if w == endWord:
                return cnt

            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    cur = w[:i] + c + w[i+1:]
                    if cur in wordSet and cur not in seen:
                        seen.add(cur)
                        q.append((cur, cnt+1))

        return 0