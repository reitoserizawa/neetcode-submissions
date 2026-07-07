class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        node = self.trie

        for l in word:
            if l not in node.children:
                node.children[l] = Node()

            node = node.children[l]

        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.trie

        for l in word:
            if l not in node.children:
                return False

            node = node.children[l]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.trie

        for l in prefix:
            if l not in node.children:
                return False
            node = node.children[l]
        
        return True