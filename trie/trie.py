class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.isLeaf = False
    

def insert(root, word):
    current = root

    