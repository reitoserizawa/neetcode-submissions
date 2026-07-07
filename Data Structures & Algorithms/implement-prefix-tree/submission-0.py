class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.trie = defaultdict(Node)

    def insert(self, word: str) -> None:
        cur = self.trie

        for l in word:
            if l not in cur:
                cur[l] = Node()

            node = cur[l]
            cur = node.children

        node.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.trie

        for l in word:
            if l not in cur:
                return False
            node = cur[l]
            cur = node.children

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie

        for l in prefix:
            if l not in cur:
                return False
            node = cur[l]
            cur = node.children
        
        return True