# Using Trie data structure O(N) - 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = set()

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.searchTerm = ""
        self.currentNode = self.root
        self.freq = {}
        for sentence, time in zip(sentences, times):
            self.addSentence(sentence, time)
    
    def addSentence(self, sentence, count):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences.add(sentence)
        self.freq[sentence] = self.freq.get(sentence, 0) + count

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        results = []
        if c == '#':
            self.addSentence(self.searchTerm, 1)
            self.searchTerm = ""
            self.currentNode = self.root
            return results
        else:
            self.searchTerm += c
            if self.currentNode:
                if c in self.currentNode.children:
                    self.currentNode = self.currentNode.children[c]
                    sentences = list(self.currentNode.sentences)
                    sentences.sort(key=lambda x: (-self.freq[x], x))
                    results = sentences[:3]
                else:
                    self.currentNode = None  # This will help in avoiding null checks
            return results


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

