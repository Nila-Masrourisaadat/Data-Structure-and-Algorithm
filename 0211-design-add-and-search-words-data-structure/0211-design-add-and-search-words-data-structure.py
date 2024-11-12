class Node():
    def __init__(self):
        self.children={}
        self.iscomplete=False

class WordDictionary(object):

    def __init__(self):
        self.root=Node()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=Node()
            node=node.children[char]
        node.iscomplete=True
       

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node,word):
            for i,char in enumerate(word):
                if char!=".":
                    if char not in node.children:
                        return False
                    node=node.children[char]
                else:
                    for child in node.children.values():
                        if dfs(child,word[i+1:]):
                            return True
                    return False
            return node.iscomplete  #only if its marked as the end of the word

        return dfs(self.root,word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)