class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        cur = self.trie

        for l in word:
            if l not in cur.children:
                cur.children[l] = Node()
            cur = cur.children[l]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.isEnd

            if not node:
                return False
            
            if word[i] == '.':    
                for (key, node) in node.children.items():
                    if dfs(i+1, node):
                        return True
            else:
                if word[i] not in node.children:
                    return False
                if dfs(i+1, node.children[word[i]]):
                    return True
            return False

        return dfs(0, self.trie)