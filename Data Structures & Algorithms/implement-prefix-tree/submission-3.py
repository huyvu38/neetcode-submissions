class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for char in word:
            #find correct place
            if char not in current.children:
                current.children[char] = TrieNode()
            current=current.children[char]
        current.isEnd=True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current=self.root
        for char in word:
            if char not in current.children:
                return False
            current=current.children[char]
        #cannot just return true because word might be just a substring
        return current.isEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current=self.root
        for char in prefix:
            if char not in current.children:
                return False
            current=current.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)