import dataclasses
@dataclasses.dataclass
class TrieNode:
    a : string
    times : int
    is_word : bool
    children : dict()

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode("", 0, False, dict())
        self.prefix = ""
        for sentence, time in zip(sentences, times):
            self.add_sentence(sentence, time)

        self.cur = self.root

    def add_sentence(self, sentence, time):
        node = self.root
        for a in sentence:
            if a not in node.children:
                node.children[a] = TrieNode(a, 0, False, dict())
            node = node.children[a]
        node.is_word = True
        node.times += time

    def input(self, c: str) -> List[str]:
        node = self.cur

        if c == "#":
            self.cur = self.root
            #print(self.prefix)
            self.add_sentence(self.prefix, 1)
            self.prefix = ""
            return []
        elif c not in node.children:
            self.prefix += c
            self.cur = TrieNode("", 0, False, dict())
            return []

        node = node.children[c]
        self.cur = node
        q = []

        def dfs(node, word):
            if node.is_word:
                heapq.heappush(q, (-node.times, word+node.a))
            for child in node.children.values():
                dfs(child, word+node.a)
        dfs(node, "")
        ret = [self.prefix + t[1] for t in heapq.nsmallest(3, q)]
        self.prefix += c
        return ret
