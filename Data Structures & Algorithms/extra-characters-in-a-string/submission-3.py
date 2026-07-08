class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.trie = Node()

        for word in dictionary:
            cur = self.trie
            for l in word:
                if l not in cur.children:
                    cur.children[l] = Node()
                cur = cur.children[l]
            cur.isEnd = True

        n = len(s)
        dp = [float('inf')] * (n+1)
        dp[-1] = 0
        
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + 1
            cur = self.trie

            for j in range(i, n):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.isEnd:
                    dp[i] = min(dp[i], dp[j+1])


        return dp[0]