class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                adj[key].append(word)

        visited = set()
        q = deque([beginWord])
        visited.add(beginWord)
        cnt = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return cnt

                for i in range(len(word)):
                    key = word[:i] + '*' + word[i+1:]
                    for child in adj[key]:
                        if child not in visited:
                            q.append(child)
                            visited.add(child)
            cnt += 1
        return 0